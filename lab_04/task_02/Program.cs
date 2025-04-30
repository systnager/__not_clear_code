using System;
using DesignPatterns.Mediator;

class Program
{
    static void Main(string[] args)
    {
        Runway runway1 = new Runway();
        Runway runway2 = new Runway();

        Aircraft aircraft1 = new Aircraft("Airplane1");
        Aircraft aircraft2 = new Aircraft("Airplane2");

        CommandCentre commandCentre = new CommandCentre(new Runway[] { runway1, runway2 }, new Aircraft[] { aircraft1, aircraft2 });


        commandCentre.LandAircraft(aircraft1, runway1);
        commandCentre.TakeOffAircraft(aircraft2, runway1);
        commandCentre.TakeOffAircraft(aircraft1, runway1);
    }
}
