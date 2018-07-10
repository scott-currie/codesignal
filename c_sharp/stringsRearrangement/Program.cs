using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace stringsRearrangement
{
    class Program
    {
        static void Main(string[] args)
        {
            //char[] a = new char[] { 'a', 'b', 'c' };
            string[] b = new string[] { "aaa", "aba", "bba", "bbb" };
            stringsRearrangement(b);
            Console.ReadKey();
        }

        static bool stringsRearrangement(string[] inputArray)
        {
            for (int i = 0; i < inputArray.Length; i++)
            {
                for (int j = 0; j < inputArray.Length; j++)
                {
                    if (i != j) {
                        if (differByOne(inputArray[i].ToCharArray(), inputArray[j].ToCharArray())) {
                            Console.WriteLine(string.Join("", inputArray[i]) + "," + string.Join("", inputArray[j]));
                        }
                    }
                }
            }
            return false;

        }

        static bool differByOne(char[] a, char[] b)
        {
            int misses = 0;
            for (int i = 0; i < a.Length; i++)
            {
                if (a[i] != b[i])
                {
                    misses++;
                    if (misses > 1)
                    {
                        return false;
                    }
                }
            }
            return true;
        }

        //static int[,] getCombinations(int[] a, int[] b)
        //{
        //    List<int> matched = new List<int>(); 
        //    for (int i = 0; i < a.Length; i++)
        //    {
        //        for (int j = 0; j < a.Length; j++)
        //        {
        //            if (!(matched.Contains(i))
        //        }
        //    }
        //}
    }
}
