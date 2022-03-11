import time
import json
from englishdart_fss_or_kr import *

if __name__ == '__main__':
    start_time = time.time()

    a = Handler()
    # final_data = a.Execute('MDA0MDAwPz1MT1RURSBGaW5lIENoZW1pY2Fs',
    #                        'Financial_Information', '', '')
    # final_data = a.Execute('SAMSUNG_ELE','','','')
    # final_data = a.Execute('samsung_ele', '', '', '')
    # samsung sds
    # final_data = a.Execute('MDE4MjYwPz1TQU1TVU5HIFNEUw===',
    #                         'Financial_Information','','')
    # samsung electr
    final_data = a.Execute('MDA1OTMwPz1TQU1TVU5HIEVMRUNUUk9OSUNT',
                            'Financial_Information','','')
    print(json.dumps(final_data, indent=4))

    elapsed_time = time.time() - start_time
    print('\nTask completed - Elapsed time: ' + str(round(elapsed_time, 2)) + ' seconds')
