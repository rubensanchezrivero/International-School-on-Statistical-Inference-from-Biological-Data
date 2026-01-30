import { Tabs, TabsContent, TabsList, TabsTrigger } from "./ui/tabs";
import programData from "../data/program.json";

export default function ProgramTabs() {
  const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];

  return (
    <Tabs defaultValue="week-0" className="w-full">
      <TabsList className="grid w-full grid-cols-2 mb-8">
        {programData.map((week, index) => (
          <TabsTrigger key={index} value={`week-${index}`}>
            {week.week}
          </TabsTrigger>
        ))}
      </TabsList>
      {programData.map((week, weekIndex) => (
        <TabsContent key={weekIndex} value={`week-${weekIndex}`}>
          <div className="overflow-x-auto">
            <table className="w-full border-collapse border border-gray-300">
              <thead>
                <tr className="bg-gray-100">
                  <th className="border border-gray-300 px-4 py-2 text-left font-semibold">
                    Time
                  </th>
                  {days.map((day) => (
                    <th
                      key={day}
                      className="border border-gray-300 px-4 py-2 text-left font-semibold"
                    >
                      {day}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {Object.entries(week.schedule).map(([time, row]) => (
                  <tr key={time} className="hover:bg-gray-50">
                    <td className="border border-gray-300 px-4 py-2 font-medium whitespace-nowrap">
                      {time}
                    </td>
                    {days.map((day) => {
                      const cell = row[day] || "";
                      const isCoffee = cell.includes("Coffee");
                      const isLunch = cell.includes("Lunch");
                      const isWorkshop = cell.includes("WORKSHOP");

                      return (
                        <td
                          key={day}
                          className={`border border-gray-300 px-4 py-2 ${
                            isCoffee ? "bg-amber-50" : isLunch ? "bg-blue-50" : isWorkshop ? "bg-green-50" : ""
                          }`}
                        >
                          {cell}
                        </td>
                      );
                    })}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </TabsContent>
      ))}
    </Tabs>
  );
}
