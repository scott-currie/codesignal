using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CheckPalindrome
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(checkPalindrome("hlbeeykoqqqqokyeeblh"));
            //string s = "tacocat";
            //if (s[1] == s[5])
            //{
            //    Console.WriteLine("True");
            //}
            //else
            //{
            //    Console.WriteLine("False");
            //}

            char a = 'i';
            char b = 'i';
            if (a == b)
            {
                Console.WriteLine("equal");
            }


            Console.ReadKey();


        }

        static bool checkPalindrome(string inputString)
        {
            /* works, but slow
            //char[] rev = inputString.ToCharArray();
            //Array.Reverse(rev);
            //string revString = new string(rev);
            //Console.WriteLine(inputString + " == " + revString);
            //if (revString.Equals(inputString))
            //{
            //    return true;
            //}
            //return false;
            */

            /* In this approach, we read from both ends toward the middle, comparing each
             * char until we either reach half the length of the string or find a pair of
             * chars that don't match.
             */
            int sLen = inputString.Length;
            int ssLen = (int)Math.Floor((double)(inputString.Length / 2));
            for (int i = 0; i < ssLen;i++)
            {
                Console.WriteLine(i + ", " + inputString[i] + " == " + inputString[sLen - i - 1]);
                if (inputString[i] != inputString[sLen - i - 1])
                {
                    return false;
                }
            }

            return true;
        } 
    }
}
