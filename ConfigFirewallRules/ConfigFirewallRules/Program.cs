using System;
using System.Collections.Generic;

namespace ConfigFirewallRules
{
    class Program
    {
        static void Main(string[] args)
        {
            
            ManageArgs manageArgs = ManageArgs.GetInstance();

            manageArgs.ParseArgs(args);

            if (!manageArgs.GetParsedData().Parsable) return;


            //foreach (string Program in manageArgs.GetParsedData().Programs) Console.WriteLine(Program);


            ManageFW Manage = new ManageFW();

            Manage.set_Disable(manageArgs.GetParsedData().DisableRule);

            List<string> ProgramList = manageArgs.GetParsedData().Programs;

            foreach (String Element in ProgramList)
            {
                Manage.set_ProgramName(Element);

                Manage.ManageRule();
            }

            //Console.ReadKey();
        }
    }
}
