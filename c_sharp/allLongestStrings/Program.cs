using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace allLongestStrings
{
    class Program
    {
        static void Main(string[] args)
        {
        }

        static string[] allLongestStrings(string[] inputArray)
        {
            int maxLen = 0;
            List<string> strings = new System.Collections.Generic.List<string>();
            foreach (string s in inputArray)
            {
                if (s.Length > maxLen)
                {
                    strings.Clear();
                    maxLen = s.Length;
                    strings.Add(s);
                }
                else if (s.Length == maxLen)
                {
                    strings.Add(s);
                }
            }

            return strings.ToArray();    
        }
    }
}
