def checkModel(self, response: dict, model: dict):

    self.assertEqual(len(model), len(response))

    for key, val in model.items():
        self.assertIn(key, response)

        # check for nullables or multi-class response types
        if type(val) is tuple:
            if response[key] is None:
                self.assertIn(None, val)
            else:
                self.assertIn(type(response[key]), val)

        # check objects nested inside a list
        elif type(val) is list:
            self.assertIsNotNone(response[key])
            self.assertGreater(len(response[key]), 0)
            for obj in response[key]:
                checkModel(self, obj, model[key][0])

        # check for enums
        elif type(val) is set:
            self.assertIn(response[key], val)

        # match type
        else:
            self.assertIsInstance(response[key], val)