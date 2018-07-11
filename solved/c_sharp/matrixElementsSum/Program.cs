using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace matrixElementsSum
{
    class Program
    {
        static void Main(string[] args)
        {
        }

        static int matrixElementsSum(int[][] matrix)
        {
            int rooms = 0;
            for (int r = 0; r < matrix.Length; r++)
            {
                for (int c = 0; c < matrix[0].Length; c++)
                {
                    if (r < matrix.Length - 1)
                    {
                        if (matrix[r][c] == 0)
                        {
                            matrix[r + 1][c] = 0;
                        }
                        else
                        {
                            rooms += matrix[r][c];
                        }
                    }
                    else
                    {
                        rooms += matrix[r][c];
                    }
                }
            }
            return rooms;
        }
    }
}
