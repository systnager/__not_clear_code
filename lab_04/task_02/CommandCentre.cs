namespace DesignPatterns.Mediator
{
    class CommandCentre
    {
        private List<Runway> _runways = new List<Runway>();
        private List<Aircraft> _aircrafts = new List<Aircraft>();

        public CommandCentre(Runway[] runways, Aircraft[] aircrafts)
        {
            this._runways.AddRange(runways);
            this._aircrafts.AddRange(aircrafts);
        }

        public void LandAircraft(Aircraft aircraft, Runway runway)
        {
            Console.WriteLine($"Checking runway for {aircraft.Name}.");
            if (!runway.IsBusy)
            {
                aircraft.Land();
                runway.IsBusy = true;
                runway.HighLightRed();
                Console.WriteLine($"{aircraft.Name} has landed on runway {runway.Id}");
            }
            else
            {
                Console.WriteLine($"Could not land {aircraft.Name}, runway is busy.");
            }
        }

        public void TakeOffAircraft(Aircraft aircraft, Runway runway)
        {
            Console.WriteLine($"Aircraft {aircraft.Name} is taking off.");
            runway.IsBusy = false;
            runway.HighLightGreen();
            aircraft.TakeOff();
            Console.WriteLine($"{aircraft.Name} has taken off from runway {runway.Id}");
        }
    }
}
