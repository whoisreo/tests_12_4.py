import logging
import unittest
from rt_with_exceptions import Runner

logging.basicConfig(level = logging.INFO, filemode = "w", filename = "runner_tests.log", encoding = "UTF-8",
                    format = "%(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            t_runner = Runner('Name', -5)
            for i in range(10):
                t_runner.walk()
            self.assertEqual(t_runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            t_runner = Runner(15)
            if not isinstance(t_runner.name, str):
                raise TypeError
            for i in range(10):
                t_runner.run()
            self.assertEqual(t_runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner")

    def test_challenge(self):
        t_runner_1 = Runner('Name_1')
        t_runner_2 = Runner('Name_2')
        for i in range(10):
            t_runner_1.run()
            t_runner_2.walk()
        self.assertNotEqual(t_runner_1.distance, t_runner_2.distance)


if __name__ == "__main__":
    unittest.main()
