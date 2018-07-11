using System;

namespace add
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(add(1, 2));
            Console.ReadKey();
        }

        static int add(int param1, int param2)
        {
            return param1 + param2;
        }
    }
}
