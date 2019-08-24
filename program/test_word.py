import unittest
import word_ladder


class word_ladder(unittest.TestCase):


    def file_load(self):
        self.assertEqual(word_ladder.file_load("test"), "\n\n The file name you have entered cannot be found -_- \n\n")



    def start_word(self):
        self.assertEqual(word_ladder.start_word("lead"), "lead")



    def target_word(self):
        self.assertEqual(word_ladder.start_word("gold"), "gold")



    def path_option(self):
        self.assertEqual(word_ladder.path_option("s"), True)


    def forbidden_build(self):
        result = word_ladder.forbidden_build("head, bead, mead")
        self.assertTrue(type(result) is list)



    def same(self):
        self.assertTrue(word_ladder.same("ate", "are") == 2)
        self.assertEqual(word_ladder.same("eat", "ate"), 0)
        self.assertEqual(word_ladder.same("test", "testing"), 4)
        self.assertEqual(word_ladder.same("1", "1"), 1)
        self.assertRaises(TypeError, word_ladder.same("test", "find"), 1)



    def build(self):
        self.assertFalse(word_ladder.build(".ead", "bead, mead, dead, head, lead", {"lead": True}, []) == False)


    def find(self):
        self.assertTrue(word_ladder.find("lead", "lead, load, goad, gold", {"lead" : True}, "gold", ["lead"]) == False)





if __name__ == '__main__':
    unittest.main()
