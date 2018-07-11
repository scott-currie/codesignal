using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ArrayTests
{
    class Program
    {
        private struct Dude
        {
            int Height = 0;
            int Weight = 0;
            string Name = "";
        }

        static void Main(string[] args)
        {

            int[] n = Enumerable.Range(1, 4).ToArray();
            Console.WriteLine(n.Length);
            //foreach (var i in n) {
                Console.WriteLine("{0} + {1} = {2}", n[0], n[1], n[2]);
            //}
            //n[3] = 1000;
            //Console.Write(Enumerable.Max(n));
            //string s = "A2";
            //char s1 = s[0];
            //int s2 = int.Parse(s[1].ToString());


            //int[] a = new int[] { 1, 2, 3, 4, 5 };
            //foreach (var n in a)
            //{
            //    n = Math.Pow(n, 2);
            //}

            //string[] s1 = new string[] { "one", "two", "three" };
            //string[] s2 = new string[] { "one", "two", "three" };
            //List<string[]> l = new List<string[]>();
            //for (int i = 0; i < 3; i++)
            //{
            //    string[] s = new string[] { i.ToString() };
            //    l.Add(s);
            //}

            //foreach (string[] s in l)
            //{
            //    Console.WriteLine(s[0]);
            //}



            //if (s1.SequenceEqual(s2))
            //{
            //    Console.WriteLine('=');
            //}

            //List<int> l = new System.Collections.Generic.List<int> {1};
            //l.RemoveAt(0);
            //Console.WriteLine(l.Count);
            //int[] a = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            //// Get sublist as copy
            //List<int> sub = new List<int>(a);
            //for (int i = 0; i < a.Length; i++)
            //{
            //     sub.RemoveAt(i);
            //    for (int j = 0; j < sub.Count - 1;j++)
            //    {
            //        if (sub[j] < sub[j + 1])
            //        {
            //            continue;
            //        }
            //        else
            //        {
            //            break;
            //        }
            //    }
            //}

            //int[][] a = new int[3][](new int[3]);
            Console.ReadKey();
        }
    }
}
