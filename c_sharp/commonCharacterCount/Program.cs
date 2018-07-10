using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace commonCharacterCount
{
    class Program
    {
        static void Main(string[] args)
        {

        }

        static int commonCharacterCount(string s1, string s2)
        {
            char[] a1 = s1.ToArray();
            //List<char> l1 = new System.Collections.Generic.List<char>(a1);
            char[] a2 = s2.ToArray();
            //List<char> l2 = new System.Collections.Generic.List<char>(a2);
            Hashtable ht1 = new Hashtable();
            Hashtable ht2 = new Hashtable();
            for (int i = 0; i < a1.Length; i++) {
                addVal(ht1, a1[i]);
            }
            for (int i = 0; i < a2.Length; i++)
            {
                addVal(ht2, a2[i]);
            }
            int total = 0;
            foreach (char c in ht1.Keys)
            {
                if (ht2.ContainsKey(c)) {
                    if ((int)ht1[c] < (int)ht2[c])
                    {
                        total += (int)ht1[c];
                    }
                    else if ((int)ht1[c] > (int)ht2[c])
                    {
                        total += (int)ht2[c];
                    }
                    else
                    {
                        total += (int)ht1[c];
                    }
                }
            }
            return total;

            
        }

        static void addVal(Hashtable ht, char c)
        {
            try
            {
                ht.Add(c, 1);
            }
            catch
            {
                ht[c] = (int)ht[c] + 1;
            }
        }
    }
}
