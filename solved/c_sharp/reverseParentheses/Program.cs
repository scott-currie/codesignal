using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace reverseParentheses
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(reverseParentheses("a(bcdefghijkl(mno)p)q"));
            Console.ReadKey();
        }

        static string reverseParentheses(string s)
        {
            List<int> lp = new System.Collections.Generic.List<int>();
            List<int> rp = new System.Collections.Generic.List<int>();
            for (int i = 0; i < s.Length; i++)
            {
                if (s[i].Equals('('))
                {
                    lp.Add(i);
                }
                if (s[i].Equals(')'))
                {
                    rp.Add(i);
                }
            }
            lp.Reverse();
            for (int i = 0; i < lp.Count; i++)
            {
                s = flip(s, lp[i], rp[i]);
            }
            return s.Replace("(","").Replace(")","");
        }


        static string flip(string s, int l, int r)
        {
            string ls = s.Substring(0, l);
            string rs = s.Substring(r);
            char[] ma = s.Substring(l, r - l).ToCharArray();
            Array.Reverse(ma);
            string ms = new string(ma);
            return ls + ms + rs;
        }
    }
}
