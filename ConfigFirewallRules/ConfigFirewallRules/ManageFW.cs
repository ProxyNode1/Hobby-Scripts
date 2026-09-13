using System;

using NetFwTypeLib; //from dependencies

namespace ConfigFirewallRules
{
    class ManageFW
    {
        //Profile
        private int Profile = (int)NET_FW_PROFILE_TYPE2_.NET_FW_PROFILE2_PRIVATE;

        //Program Data
        private string ProgramName;
        private bool Disable;

        //create an object
        private INetFwPolicy2 FirewallPolicy = (INetFwPolicy2)Activator.CreateInstance(Type.GetTypeFromProgID("HNetCfg.FwPolicy2"));


        public void set_ProgramName(string ProgramName)
        {
            this.ProgramName = ProgramName;

            Console.WriteLine("Program Name: " + this.ProgramName);
        }

        public void set_Disable(bool Disable)
        {
            this.Disable = Disable;

            Console.WriteLine("Disable: " + this.Disable);
        }

        public void ManageRule()
        {
            foreach (INetFwRule Rule in FirewallPolicy.Rules)
            {
                // look for rule with the provided name
                if (Rule.Name == ProgramName)
                {
                    //Console.Write(Rule.Name);

                    //look for all private profile
                    if (Rule.Profiles == Profile)
                    {
                        //enable/disable the rule
                        Rule.Enabled = !Disable;
                    }
                }
            }
        }
    }
}
