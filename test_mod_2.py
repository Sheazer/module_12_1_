import module_12_2 as mod
import unittest


class test_runner(unittest.TestCase):

    def test_walk(self):
        runner = mod.Runner('Erzhan')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = mod.Runner('Erzhan')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        first_runner = mod.Runner("Vova")
        secont_runner = mod.Runner('Petya')
        for _ in range(10):
            first_runner.run()
            secont_runner.walk()
            self.assertNotEqual(first_runner.distance, secont_runner.distance)