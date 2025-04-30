namespace DesignPatterns.Mediator
{
    class Aircraft
    {
        public string Name;
        public bool IsTakingOff { get; set; }

        public Aircraft(string name)
        {
            this.Name = name;
        }

        public void Land()
        {
            Console.WriteLine($"Aircraft {this.Name} is landing.");
        }

        public void TakeOff()
        {
            Console.WriteLine($"Aircraft {this.Name} is taking off.");
        }
    }
}
