using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace boxBlur
{
    class Program
    {
        static void Main(string[] args)
        {
            int[][] img = new int[7][];
            img[0] = new int[] { 36, 0, 18, 9, 9, 45, 27 };
            img[1] = new int[] { 27, 0, 54, 9, 0, 63, 90 };
            img[2] = new int[] { 81, 63, 72, 45, 18, 27, 0 };
            img[3] = new int[] { 0, 0, 9, 81, 27, 18, 45};
            img[4] = new int[] { 45, 45, 27, 27, 90, 81, 72 };
            img[5] = new int[] { 45, 18, 9, 0, 9, 18, 45 };
            img[6] = new int[] { 27, 81, 36, 63, 63, 72, 81 };

            int[][] blurred = boxBlur(img);

            blurred = FrameArray(blurred);

            printArrays(blurred);

            Console.ReadKey();
        }

        static int[][] boxBlur(int[][] image)
        {
            int[][] blurred = new int[image.Length][];
            for (int row = 0; row < image.Length;row++)
            {
                blurred[row] = new int[image[0].Length];
            }


            for (int row = 1; row < image.Length - 1; row++)
            {
                for (int col = 1; col < image[0].Length - 1; col++)
                {
                    int boxSum = 0;
                    for (int i = -1; i < 2; i++)
                    {
                        for (int j = -1; j < 2; j++)
                        {
                            boxSum += image[row + i][col + j];
                        }
                    }
                    int boxAvg = (int)(boxSum / 9);
                    blurred[row][col] = boxAvg;
                }
            }
            return blurred;
        }

        static void printArrays(int[][] a)
        {
            for (int row = 0; row < a.Length;row++)
            {
                for (int col = 0;col < a[0].Length; col++) {
                    Console.Write(a[row][col]);
                    Console.Write(",");
                }
                Console.WriteLine();
            }
        }

        static int[][] FrameArray(int[][]a)
        {
            int[][] framed = new int[a.Length - 2][];
            for (int i = 1; i < a.Length - 1;i++)
            {
                framed[i - 1] = new int[a[0].Length - 2];
                for (int j = 1; j < a[0].Length - 1; j++)
                {
                    framed[i - 1][j - 1] = a[i][j];
                }
            }
            return framed;
        }
    }
}
