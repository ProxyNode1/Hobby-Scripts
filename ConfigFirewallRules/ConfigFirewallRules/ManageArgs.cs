using System;
using System.Collections.Generic;

using Mono.Options; //from dependencies

namespace ConfigFirewallRules
{
    struct ArgData
    {
        public bool DisableRule;

        public List<string> Programs;

        public bool Parsable;

        public ArgData(bool DisableRule, List<string> Programs, bool Parsable)
        {
            this.DisableRule = DisableRule;
            this.Programs = Programs;
            this.Parsable = Parsable;
        }
    }

    class ManageArgs
    {

        private static readonly ManageArgs Instance = new ManageArgs();

        private ManageArgs() { }

        public static ManageArgs GetInstance()
        {
            return Instance;
        }


        static private bool ShouldShowHelp = false;

        static private List<string> Programs = new List<string>();

        static private bool IsDisableArgProvided = false;

        static bool Disable = false;


        static OptionSet options = new OptionSet
            {
                { "h|help",
                  @"Should allow a program to connect to the Internet.",
                  h => ShouldShowHelp = h != null
                },

                { "p|programs=", "Program/s to manage. Input: \"Program1Name\" or \"Program1Name, Program2Name\". Name should be case-sensitive.",
                    n => {
                        if(n != null)
                        {
                            String[] str = n.Split(", ");
                            Programs = new List<String>(str);
                        }
                    }
                },

                { "a|allow=", "Allow the program through firewall. Input: true/false",
                    a => {
                    if(a != null)
                    {
                            Disable = bool.Parse(a);
                            IsDisableArgProvided = true;
                    } } }
            };

        public void ParseArgs(string[] args)
        {
            options.Parse(args);

            if (ShouldShowHelp) options.WriteOptionDescriptions(Console.Out);
        }

        public ArgData GetParsedData()
        {
            return new ArgData(Disable, Programs, Programs.Count != 0 && IsDisableArgProvided);
        }
    }
}
