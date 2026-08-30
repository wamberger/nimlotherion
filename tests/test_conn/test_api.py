import json
import os
import sys
import unittest
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

import nimlotherion as sl


class TestApi(unittest.TestCase):

    def test_api(self):


        config = sl.config('yaml', 'C:\\Users\\awa\\work_desk\\projects\\nimlotherion\\tests\\_test_utility_files\\test_config.yaml')

        cfg = config['rest_evo']

        rest = sl.RESTapiSession(
            domain=cfg['domain'],
            path=cfg['path_l'],
            user=cfg['user'],
            password=cfg['password'],
            headers=cfg['headers_l'])

        r1 = rest.post(allow_redirects=True)

        rest.update_headers(cfg['headers_p'])
        rest.update_path(cfg['path_p_persst'])
        json_data = "{}"
        r2 = rest.post(data=json_data)

        rest.update_path(cfg['path_g_persst'])
        rest.update_params("?persNr=9000&datum=20240425")
        r3 = rest.get()

        a = r3.content
        b = a.decode(r3.encoding)
        c = json.loads(b)
        a = 1


if __name__ == '__main__':
    unittest.main()