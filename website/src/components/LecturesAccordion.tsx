import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "./ui/accordion";
import lecturesData from "../data/lectures.json";

export default function LecturesAccordion() {
  return (
    <Accordion type="single" collapsible className="w-full">
      {lecturesData.map((block, index) => {
        const header = block.lecturers
          .map((l) => {
            if (l.topic && l.name && l.affiliation) {
              return `${l.topic} (${l.name}, ${l.affiliation})`;
            } else if (l.affiliation) {
              return `${l.name} (${l.affiliation})`;
            } else {
              return l.name;
            }
          })
          .join(", ");

        return (
          <AccordionItem key={index} value={`item-${index}`}>
            <AccordionTrigger className="text-left">
              <span className="font-semibold">{header}</span>
            </AccordionTrigger>
            <AccordionContent>
              <div className="space-y-4">
                {block.lectures.map((lec, lecIndex) => (
                  <div key={lecIndex} className="pl-4 border-l-2 border-gray-200">
                    <p className="font-medium text-gray-900">
                      {lec.label && <span className="font-semibold">{lec.label}: </span>}
                      {lec.title}
                    </p>
                    {lec.subtitle && (
                      <p className="text-sm text-gray-600 mt-1">{lec.subtitle}</p>
                    )}
                  </div>
                ))}
              </div>
            </AccordionContent>
          </AccordionItem>
        );
      })}
    </Accordion>
  );
}
