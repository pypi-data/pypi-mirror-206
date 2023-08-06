from typing import Union

from functools import lru_cache
import json
from tqdm import tqdm
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests


class Client:

    def __init__(self, language="en", 
                 api="https://wikidata.reconci.link/",
                 threads=4) -> None:
        """Create a new Client.

        The client class handles everything for reconciliation and deals with 
        concurrent connections.

        Currently, only supports 'https://wikidata.reconci.link/' endpoints

        Args:
            language (str, optional): Set the language of your search terms. Defaults to "en".
            api (str, optional): URL to API endpoint. Defaults to "https://wikidata.reconci.link/".
            threads (int, optional). Number of concurrent requests (more is faster, but might cause server to reject your requests). Defaults to 4.
        """

        if not api.endswith('/'):
            api += '/'

        self._api = api + language + '/api'
        self._language = language
        self._threads = threads

    def reconcile(self,
                  data: Union[list, dict, pd.DataFrame],
                  property_mapping: dict=None,
                  limit=50) -> list:
        """Main method for reconciling a collection of data.

        You can supply a list of dicts, a single dict, or a pandas dataframe.
        The required key for your dicts (or dataframe) is 'query' which is 
        the search string you want to look up at the reconciliation endpoint.

        You can additionally, provide the key 'type' to reconcile a specific type 
        (e.g. 'Q5' for humans). Then the client will request wikidata entries that 
        match against this type ("find me all entries with query keyword 'X' and are instance of 'Q5'")

        A wrapper for the `Client.query()` method
        
        Args:
            data (Union[list, dict, pd.DataFrame]): Your input data.
            property_mapping (dict, optional): A property matching dictionary for a pandas dataframe. 
                In the style of {'<Column Name>': '<Wikidata Property>'}. Ex. {'country': 'P17'}. Defaults to None.
            limit (int, optional): Maximum number of results returned per query. Defaults to 50.

        Returns:
            list: A list of dicts where each dict represents a query result. 
        """
        if isinstance(data, pd.DataFrame):
            data = self.pandas_to_query(
                data, limit=limit, property_mapping=property_mapping)
        elif isinstance(data, dict):
            data = [data]

        return self.query(data)

    def query(self, data: list) -> list:
        """Concurrent query Wikidata (or reconciliation service) 

        Args:
            data (list): a list of dicts where each dict is a query.

        Returns:
            list: a list of dicts where ach dict is the reconciled response.
        """        
        results = []
        with tqdm(total=len(data), unit="queries", desc="Reconciling") as pbar:
            with ThreadPoolExecutor(max_workers=self._threads) as executor:
                tasks = [executor.submit(self._single_query, q) for q in data]
                for future in as_completed(tasks):
                    results.append(future.result())
                    pbar.update(1)

        return results

    @lru_cache(maxsize=None)
    def _perform_single_query(self,
                                query: str,
                                search_string: str,
                                max_retries=10,
                                fallback_searchstring: bool = False) -> dict:
        """ low level function to performa a single query.

        Args:
            query (str): a serialized JSON dict (generated with `json.dumps(data)`)
            search_string (str): the original search query.
            max_retries (int, optional): Maximum attempts to retry. Defaults to 10.
            fallback_searchstring (bool, optional): Used for managing recursive calls.
        Returns:
            dict: A single query result
        """        

        formatted_query = {"query": query}
        tries = 0
        while tries < max_retries:
            try:
                r = requests.get(self._api, params=formatted_query)
                r.raise_for_status()
                j = r.json()
                j['search_string'] = search_string
                if "status" in j and j["status"] == "error":
                    if tries == max_retries - 1:
                        return {'search_string': search_string, 'result': [], 'status': j['status']}
                    tries += 1
                    continue
                # What actions to perform when there is no result?
                if len(j['result']) == 0:
                    query = json.loads(query)
                    # if a fallback query is specified, try that one first
                    if 'fallback_query' in query:
                        query["query"] = query.pop("fallback_query")
                        return self._perform_single_query(json.dumps(query), search_string)
                    # if the search query has hyphens, we try to search for the first element instead
                    if "-" in search_string and not fallback_searchstring:
                        query["query"] = search_string.split("-")[0]
                        return self._perform_single_query(json.dumps(query), search_string, fallback_searchstring=True)
                    # try to match against no type
                    elif "type" in query:
                        _ = query.pop("type")
                        return self._perform_single_query(json.dumps(query), search_string)
                return j

            except (requests.ConnectionError, requests.ConnectTimeout):
                tries += 1
            except Exception as e:
                return {'search_string': search_string, 'result': [], 'error': e}

        if tries == max_retries:
            return {'search_string': search_string, 'result': [], 'error': 'Too many retries'}

    def _single_query(self, query: dict) -> dict:
        """Wrapper to prepare a dict for `_perform_single_query()` method.

        Args:
            query (dict): A single query dictionary.

        Returns:
            dict: A single query result
        """        

        search_string = query['query']

        return self._perform_single_query(json.dumps(query), search_string)

    @staticmethod
    def pandas_to_query(df: pd.DataFrame, limit=50, property_mapping: dict = None) -> list:
        """Transform a pandas dataframe to a list of dicts

        You can additionally, provide the key 'type' to reconcile a specific type 
        (e.g. 'Q5' for humans). Then the client will request wikidata entries that 
        match against this type ("find me all entries with query keyword 'X' and 
        are instance of 'Q5'")

        If you have additional columns that match against wikidata properties 
        (e.g., 'P17' for countries), you can provide a property mapping dictionary in 
        the style of {'<Column Name>': '<Wikidata Property>'}. Ex. {'country': 'P17'}.
        The values in the property column have to be Wikidata IDs (e.g., 'Q17' for 'Japan').

        Args:
            df (pd.DataFrame): A dataframe with the required column 'query'. 
                Optional column is 'type'.
            limit (int, optional): Maximum number of results per query. Defaults to 50.
            property_mapping (dict, optional): A dictionary to map columns against properties. 
                Defaults to None.

        Returns:
            list: A list of dicts where each represents one query.
        """        
        assert "query" in df.columns, "No column 'query' provided!"

        cols = ["query", "limit"]
        if "type" in df.columns:
            cols.append('type')

        _df = df.copy(deep=True)

        _df['limit'] = limit

        if property_mapping:
            for col, property in property_mapping.items():
                _df[property] = [{'pid': property, 'v': i}
                                 for i in _df[col].to_list()]

            _df['properties'] = _df.loc[:, list(
                property_mapping.values())].values.tolist()

            cols.append('properties')

        data = _df.loc[:, cols].to_dict(orient='records')
        return data

    @staticmethod
    def results_to_pandas(result: list, top_res: Union[int, None] = 1) -> pd.DataFrame:
        """Reformat results to a dataframe.

        Utility function to turn the list of dicts back into a pandas dataframe.

        Args:
            result (list): list of dicts with query results.
            top_res (Union[int, None], optional): Only keep the top number of results. Defaults to 1.

        Returns:
            pd.DataFrame: A dataframe with the columns: `search_string`, `match`, `score`, `name`,
                `id`, `description`, `type_id`, `type_description`
        """        
        
        dfs = []
        for r in result:

            try:
                current_df = pd.json_normalize(r["result"])
            except:
                current_df = pd.DataFrame({"id": [""], "match": [False]})

            if current_df.empty:
                current_df = pd.DataFrame({"id": [""], "match": [False]})
            else:
                try:
                    current_df.drop(columns=["features"], inplace=True)
                    current_df["type_id"] = [item[0]["id"]
                                             for item in current_df["type"]]
                    current_df["type_description"] = [item[0]["name"]
                                                      for item in current_df["type"]]
                except (IndexError, KeyError):
                    pass

            current_df["search_string"] = r['search_string']
            dfs.append(current_df)

        concatenated = pd.concat(dfs, ignore_index=True)
        reordered_cols = ['search_string', 'match', 'score', 'name',
                          'id', 'description', 'type_id', 'type_description']
        concatenated = concatenated.loc[:, reordered_cols]
        if not top_res:
            return concatenated
        else:
            return concatenated.groupby("search_string").head(top_res).reset_index(drop=True)
