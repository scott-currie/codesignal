using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace areSimilar
{
    class Program
    {
        static void Main(string[] args)
        {
            Random rand = new Random();
            for (int i = 0; i < 10000; i++)
            {
                int[] a1 = new int[rand.Next(3, (int)Math.Pow(10,5))];
                for (int j = 0; j < a1.Length; j++)
                {
                    a1[j] = rand.Next(1, 1000);
                }
                int[] a2 = new int[a1.Length];
                Array.Copy(a1, a2, a1.Length);
                if (rand.Next(0, 1) == 0)
                {
                    a1 = swapRand(a1);
                }
                else
                {
                    a2 = swapRand(a2);
                }
                //int[] a1 = new int[] { 1, 2, 3 };
                //int[] a2 = new int[] { 2, 1, 3 }; 
                if (!(areSimilar(a1, a2)))
                {
                    Console.WriteLine("Not similar!");
                    //writeArray(a1);
                    //writeArray(a2);
                }
            }
            Console.WriteLine("All done!");
            Console.ReadKey();
        }

        static bool areSimilar(int[] a, int[] b)
        {
            if (a.SequenceEqual(b))
            {
                return true;
            }
            //string sep = "===============================================================";
            //Console.WriteLine(sep);
            //Console.Write("a = ");
            //writeArray(a);
            //Console.Write("b = ");
            //writeArray(b);
            for (int i = 0; i < a.Length; i++)
            {
                if (a[i] != b[i])
                {
                    /* Here's where we start making comparisons, but we assume that there
                     * will only ever be on pair of subarrays. If one of the values to swap
                     * appears more than once in the array, we'll need to try swapping all of
                     * which will mean handling comparing multiple subarrays.
                     */
                    //GET SUBARRAYS FIRST, SINCE WE KNOW WHERE THE PROBLEM STARTS
                    int[] aSubArray = new int[a.Length - i];
                    Array.Copy(a, i, aSubArray, 0, aSubArray.Length);
                    int[] bSubArray = new int[b.Length - i];
                    Array.Copy(b, i, bSubArray, 0, bSubArray.Length);
                    //Console.Write("aSubArray = ");
                    //writeArray(aSubArray);
                    //Console.Write("bSubArray = ");
                    //writeArray(bSubArray);

                    if (aSubArray.Length <= 1)
                    {
                        return false;
                    }

                    // Get indices in a of all occurrences of the current value at b
                    List<int> aIndices = getIndices(aSubArray, bSubArray[0]);
                    // Get indices in b of all occurrences of the current value at a
                    List<int> bIndices = getIndices(bSubArray, aSubArray[0]);

                    List<int[]> aSubs = getSwappedArrays(aSubArray, aIndices);
 
                    List<int[]> bSubs = getSwappedArrays(bSubArray, bIndices);


                    foreach (int[] aSub in aSubs)
                    {
                        //Console.Write("aSub = ");
                        //writeArray(aSub);
                        //Console.Write("bSubArray = ");
                        //writeArray(bSubArray);

                        if (aSub.SequenceEqual(bSubArray))
                        {
                            return true;
                        }
                    }
                    foreach (int[] bSub in bSubs)
                    {
                        //Console.Write("bSub = ");
                        //writeArray(bSub);
                        //Console.Write("aSubArray = ");
                        //writeArray(bSubArray);
                        if (bSub.SequenceEqual(aSubArray))
                        {
                            return true;
                        }
                    }

                    return false;
                }
            }
            return false;
        }

        static int[] swapRand(int[] a) 
        {
            Random r = new Random();
            int i1 = r.Next(0, a.Length - 1);
            int i2 = r.Next(0, a.Length - 1);
            int tmp = a[i1];
            a[i1] = a[i2];
            a[i2] = tmp;
            return a;
        }

        static void writeArray(int[] a)
        {
            Console.WriteLine(String.Join(",", a));
        }

        static List<int> getIndices(int[] arr, int val)
        {
            List<int> indices = new System.Collections.Generic.List<int>();
            for (int i = 0;i < arr.Length;i++)
            {
                if (arr[i] == val)
                {
                    // I want to adjust these indices relative to the start of the subarrays
                    indices.Add(i);
                }
            }
            return indices;
        }

        static List<int[]> getSwappedArrays(int[] a, List<int> indices)
        {
            List<int[]> swappedArrays = new System.Collections.Generic.List<int[]>();
            foreach (int i in indices)
            {
                // HERE'S WHERE WE ROLL UP SUBARRAYS
                int[] subArray = new int[a.Length];
                Array.Copy(a, subArray, subArray.Length);
                // HERE'S WHERE WE SWAP THE ELEMENTS
                swapElements(subArray, 0, i);
                //HERE'S WHERE WE ADD THE SWAPPED SUBARRAYS TO THE RETURN LIST
                swappedArrays.Add(subArray);
            }
            return swappedArrays;
        }

        static void swapElements(int[] a, int i, int j)
        {
            int tmp = a[i];
            a[i] = a[j];
            a[j] = tmp;
        }
    }
}
