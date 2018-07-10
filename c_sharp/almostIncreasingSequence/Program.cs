using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace almostIncreasingSequence
{
    class Program
    {
        static void Main(string[] args)
        {
            
        }

        bool almostIncreasingSequence(int[] sequence)
        {

            if (sequence.Length == 2)
            {
                return true;
            }
            int startI = 0;
            for (int i = 0; i < sequence.Length - 1; i++)
            {
                if (sequence[i] > sequence[i + 1])
                {
                    startI = i;
                    break;
                }
            }

            for (int i = startI; i < sequence.Length; i++)
            {
                List<int> sub = new List<int>(sequence);
                sub.RemoveAt(i);
                foreach (int j in sub)
                {
                    Console.Write(j.ToString() + ",");
                }
                Console.WriteLine();
                for (int j = 0; j < sub.Count - 1; j++)
                {
                    if (sub[j] >= sub[j + 1])
                    {
                        break;
                    }
                    // If you get here, you've had a clean pass, so that's good enough.
                    if (j == sub.Count - 2)
                    {
                        return true;
                    }
                }
            }
            // If you get here, you never had a clean pass, so return false.
            return false;
        }
    }
}
