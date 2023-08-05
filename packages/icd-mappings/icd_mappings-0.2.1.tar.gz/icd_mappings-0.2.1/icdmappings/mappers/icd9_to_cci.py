from typing import List, Union
import os
from collections.abc import Iterable
import csv
import importlib.resources
from icdmappings import data_files

class ICD9toCCI:
        """
        Maps icd9 diagnostic codes to chronic or not chronic (that is the question).
        
        source of mapping: https://www.hcup-us.ahrq.gov/toolssoftware/chronic/chronic.jsp
        """
        def __init__(self):
            self.filename = "cci2015.csv"
            self.icd9_to_cci = None # will be filled by self._setup() {icd9code:cci,...icd9code:cci}
            self._setup()


        def _setup(self):
            # creates self.chapters_num, self.chapters_char, self.bins
            self.icd9_to_cci = self._parse_file(self.filename)


        def map(self,
                icd9code : Union[str, Iterable]
                ):
                """
                Given an icd9 code, returns the corresponding Chronic value (True for chronic, and False for not-chronic)

                Parameters
                ----------

                code : str | pd.Series
                    icd9 code

                Returns:
                    -1: code is not recognizable
                    True: When the code is chronic
                    False: when the code is not chronic
                """
                def map_single(icd9code : str):
                    try:
                        return self.icd9_to_cci[icd9code]
                    except:
                        return None

                if isinstance(icd9code, str):
                    return map_single(icd9code)
                elif isinstance(icd9code, Iterable):
                    return [map_single(c) for c in icd9code]
                else:
                     raise TypeError(f'Wrong input type. Expecting str or Iterable. Got {type(icd9code)}')


        def _parse_file(self, filename : str):
            with importlib.resources.open_text(data_files, filename) as csvfile:
                reader = csv.reader(csvfile, quotechar="'")
                headers = next(reader)

                cci_to_bool = {'1':True,'0':False}

                mapping = {}

                for row in reader:
                    icd9_code = row[0].strip()
                    cci = cci_to_bool[row[2]]
                    mapping[icd9_code] = cci

            return mapping