using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace centuryFromYear
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(centuryFromYear(1905));
            Console.ReadKey();
        }

        static int centuryFromYear(int year)
        {
            decimal c = Math.Ceiling((decimal)year / 100);
            return (int)c;
        }
    }
}
