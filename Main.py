import glob
import os
from datetime import datetime

import pandas as pd
from matplotlib import pyplot as plt

from ReadContent import ReadContent
from RulesAndFilters import RulesAndFilters

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "input files/*")

# df = pd.read_csv("/home/amirhossein/Documents/GitHub/new-temp/input files/pollutionData158355.csv", index_col=False)
# df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d %H:%M:%S')
# df.sort_values('timestamp', inplace=True)
# df.to_csv('result.csv', index=False)


for file in glob.glob(path):
    if ReadContent.getFileFormat(file) == "txt":
        readContent = ReadContent(file)

for file in glob.glob(path):
    if ReadContent.getFileFormat(file) == "csv":
        print("file is: ", file)

        # rulesAndFilters = RulesAndFilters(file)
        # rulesAndFilters.removeRowsThatViolateAllConditions([
        #                             {"header": "vehicleCount", "value": 0, "condition": "not equal"},
        #                             {"header": "avgSpeed", "value": 60, "condition": "smaller than"},
        #                             {"header": "sulfure_dioxide", "value": 60, "condition": "smaller than"}])
        #
        # rulesAndFilters.removeDuplicateRowsFromCSV()
        # rulesAndFilters.setValueRange("vehicleCount", 0, condition="not equal")
        # rulesAndFilters.setValueRange("avgSpeed", 60, condition="smaller than")
        # rulesAndFilters.checkTypeOfValue("avgSpeed", int)
        # rulesAndFilters.removeInvalidTimeStamps()
        # rulesAndFilters.removeTimeStampsNotDividableBy5()

        # readContent = ReadContent(file)
        # readContent.createFormattedAddressColumn()
        #
        # readContent.plotFromBarChartForOneCSV("vehicleCount", "avgSpeed", "sulfure_dioxide", "carbon_monoxide",
        #                                       "particullate_matter", "nitrogen_dioxide")
        # print("Avg is : ", readContent.getAvgValueOfColumn("avgMeasuredTime"))
        # print("min is : ", readContent.getMinValueOfColumn("avgSpeed"))
        # print("max is : ", readContent.getMaxValueOfColumn("avgSpeed"))
        # print("first row is : ", readContent.getFirstRow())
        # print("last row is : ", readContent.getLastRow())
        # print("headers are : ", readContent.getHeaders())
        # print("number of rows is : ", readContent.getSize(), "\n")

# ReadContent.plotLineChart(["pollutionData158324.csv", "pollutionData158355.csv"], "carbon_monoxide")
# ReadContent.plotOneLineChartFromMultipleFiles(["pollutionData158324.csv", "pollutionData158355.csv"],
#                                               ["carbon_monoxide", "vehicleCount"])


# ReadContent.plotCustomLineCharts(["pollutionData158324.csv", "particullate_matter"],
#                                  ["pollutionData158324.csv", "carbon_monoxide"],
#                                  ["pollutionData158324.csv", "sulfure_dioxide"],
#                                  ["pollutionData158324.csv", "nitrogen_dioxide"], format='one by one')
#
# ReadContent.plotCustomLineCharts(["pollutionData158324.csv", "carbon_monoxide"],
#                                  ["pollutionData158355.csv", "carbon_monoxide"], format='one by one')

ReadContent.plotCustomLineCharts(["trafficData158324.csv", "avgSpeed"],
                                 ["trafficData158324.csv", "vehiclecount"],
                                 format='one by one')