from .bo.eventBOs.EventBO import EventBO
from .db.eventMapper.EventMapper import EventMapper
from .bo.eventBOs.ComingBO import ComingBO
from .db.eventMapper.ComingMapper import ComingMapper
from .bo.eventBOs.GoingBO import GoingBO
from .db.eventMapper.GoingMapper import GoingMapper
from .bo.eventBOs.VacationBeginBO import VacationBeginBO
from .db.eventMapper.VacationBeginMapper import VacationBeginMapper
from .bo.eventBOs.VacationEndBO import VacationEndBO
from .db.eventMapper.VacationEndMapper import VacationEndMapper
from .bo.eventBOs.IllnessBeginBO import IllnessBeginBO
from .db.eventMapper.IllnessBeginMapper import IllnessBeginMapper
from .bo.eventBOs.IllnessEndBO import IllnessEndBO
from .db.eventMapper.IllnessEndMapper import IllnessEndMapper
from .bo.eventBOs.ProjectWorkBegin import ProjectWorkBeginBO
from .db.eventMapper.ProjectWorkBeginMapper import ProjectWorkBeginMapper
from .bo.eventBOs.ProjectWorkEnd import ProjectWorkEndBO
from .db.eventMapper.ProjectWorkEndMapper import ProjectWorkEndMapper
from .bo.eventBOs.BreakBeginBO import BreakBeginBO
from .db.eventMapper.BreakBeginMapper import BreakBeginMapper
from .bo.eventBOs.BreakEndBO import BreakEndBO
from .db.eventMapper.BreakEndMapper import BreakEndMapper
from .bo.eventBOs.EventBO import EventBO
from .db.eventMapper.EventMapper import EventMapper
from .bo.eventBOs.ComingBO import ComingBO
from .db.eventMapper.ComingMapper import ComingMapper
from .bo.eventBOs.GoingBO import GoingBO
from .db.eventMapper.GoingMapper import GoingMapper
from .bo.eventBOs.VacationBeginBO import VacationBeginBO
from .db.eventMapper.VacationBeginMapper import VacationBeginMapper
from .bo.eventBOs.VacationEndBO import VacationEndBO
from .db.eventMapper.VacationEndMapper import VacationEndMapper
from .bo.eventBOs.IllnessBeginBO import IllnessBeginBO
from .db.eventMapper.IllnessBeginMapper import IllnessBeginMapper
from .bo.eventBOs.IllnessEndBO import IllnessEndBO
from .db.eventMapper.IllnessEndMapper import IllnessEndMapper
from .bo.eventBOs.ProjectWorkBegin import ProjectWorkBeginBO
from .db.eventMapper.ProjectWorkBeginMapper import ProjectWorkBeginMapper
from .bo.eventBOs.ProjectWorkEnd import ProjectWorkEndBO
from .db.eventMapper.ProjectWorkEndMapper import ProjectWorkEndMapper
from .bo.eventBOs.BreakBeginBO import BreakBeginBO
from .db.eventMapper.BreakBeginMapper import BreakBeginMapper
from .bo.eventBOs.BreakEndBO import BreakEndBO
from .db.eventMapper.BreakEndMapper import BreakEndMapper
from .bo.eventBOs.FlexDayStart import FlexDayStartBO
from .db.eventMapper.FlexDayStartMapper import FlexDayStartMapper
from .bo.eventBOs.FlexDayEndBO import FlexDayEndBO
from .db.eventMapper.FlexDayEndMapper import FlexDayEndMapper

from .bo.BookingBO import BookingBO
from .db.BookingMapper import BookingMapper
from .bo.EventBookingBO import EventBookingBO
from .db.EventBookingMapper import EventBookingMapper
from .bo.TimeIntervalBookingBO import TimeIntervalBookingBO
from .db.TimeIntervalBookingMapper import TimeIntervalBookingMapper
from .bo.timeinterval.TimeIntervalBO import TimeIntervalBO
from .db.timeinterval.TimeIntervalMapper import TimeIntervalMapper
from .bo.timeinterval.BreakBO import BreakBO
from .db.timeinterval.BreakMapper import BreakMapper
from .bo.timeinterval.IllnessBO import IllnessBO
from .db.timeinterval.IllnessMapper import IllnessMapper
from .bo.timeinterval.ProjectDurationBO import ProjectDurationBO
from .db.timeinterval.ProjectDurationMapper import ProjectDurationMapper
from .bo.timeinterval.ProjectWorkBO import ProjectWorkBO
from .db.timeinterval.ProjectWorkMapper import ProjectWorkMapper
from .bo.timeinterval.VacationBO import VacationBO
from .db.timeinterval.VacationMapper import VacationMapper
from .bo.timeinterval.WorkBO import WorkBO
from .db.timeinterval.WorkMapper import WorkMapper
from .bo.timeinterval.FlexDayBO import FlexDayBO
from .db.timeinterval.FlexDayMapper import FlexDayMapper
from datetime import datetime
from .bo.UserBO import UserBO
from .db.UserMapper import UserMapper
from .bo.WorkTimeAccountBO import WorkTimeAccountBO
from .db.WorkTimeAccountMapper import WorkTimeAccountMapper
from .bo.ProjectBO import ProjectBO
from .db.ProjectMapper import ProjectMapper
from .bo.ProjectUserBO import ProjectUserBO
from .db.ProjectUserMapper import ProjectUserMapper
from .bo.ActivityBO import ActivityBO
from .db.ActivityMapper import ActivityMapper


import math


class Businesslogic:
    def __init__(self):
        pass

    """Beginn der Event-& und Evensubklassenmethoden"""
    """Author: Khadidja Kebaili"""
    def create_event(
        self,
        type,
        coming_id,
        going_id,
        break_begin_id,
        break_end_id,
        illness_begin_id,
        illness_end_id,
        project_work_begin_id,
        project_work_end_id,
        vacation_begin_id,
        vacation_end_id,
        flex_day_start_id,
        flex_day_end_id,
    ):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Erstellung eines EventBOs mit Typ des Events und jeweils einen Fremdschlüssel
        :param type: Event-Typ
        :param coming_id: Fremdschlüssel ComingBO
        :param going_id: Fremdschlüssel GoingBO
        :param break_begin_id: Fremdschlüssel BreakBeginBO
        :param break_end_id: Fremdschlüssel BreakEndBO
        :param illness_begin_id: Fremdschlüssel IllnessBeginBO
        :param illness_end_id: Fremdschlüssel IllnessEndBO
        :param project_work_begin_id: Fremdschlüssel ProjectWorkBeginBO
        :param project_work_end_id: Fremdschlüssel ProjectWorkEndBO
        :param vacation_begin_id: Fremdschlüssel VacationBeginBO
        :param vacation_end_id: Fremdschlüssel VacationEndBO
        :param flex_day_start_id: Fremdschlüssel FlexDayStartBO
        :param flex_day_end_id: Fremdschlüssel FlexDayEndBO
        :return: EventBO mit Typ und einem Fremdschlüssel, restliche Parameter sind null-Werte
        """
        event = EventBO()
        event.set_type(type),
        event.set_coming_id(coming_id),
        event.set_going_id(going_id),
        event.set_break_begin_id(break_begin_id),
        event.set_break_end_id(break_end_id),
        event.set_illness_begin_id(illness_begin_id),
        event.set_illness_end_id(illness_end_id),
        event.set_project_work_begin_id(project_work_begin_id),
        event.set_project_work_end_id(project_work_end_id),
        event.set_vacation_begin_id(vacation_begin_id),
        event.set_vacation_end_id(vacation_end_id)
        event.set_flex_day_start_id(flex_day_start_id)
        event.set_flex_day_end_id(flex_day_end_id)
        with EventMapper() as mapper:
            return mapper.insert(event)

    def get_event_by_id(self, id):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um ein EventBO mit bestimmter ID aus der Datenbank zu laden
        :param id: EventBO-ID
        :return: EventBO
        """
        with EventMapper() as mapper:
            return mapper.find_by_key(id)

    def get_all_events(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um alle EventBOs aus der Datenbank zu laden
        :return: Array mit EventBOs
        """
        with EventMapper() as mapper:
            return mapper.find_all()

    def get_all_events_by_type(self, type):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um EventBOs mit bestimmten Typ aus der Datenbank zu laden
        :param type: Typ der Eventsubklasse (bspw. breakbegin)
        :return: Array mit EventBOs
        """
        events = self.get_all_events()
        events_of_type = []
        for elem in events:
            if elem.get_type == type:
                events_of_type.append(elem)
        return events_of_type

    def save_event(self, event):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        EventBO aus der Datenbank laden, updaten und speichern.
        :param event: EventBO
        """
        with EventMapper() as mapper:
            mapper.update(event)

    def delete_event(self, event):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um ein EventBO aus der Datenbank zu entfernen
        :param event: EventBO
        :return: EventBO
        """
        with EventMapper() as mapper:
            mapper.delete(event)

    def create_coming(self, time):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

         Erstellung eines ComingBOs, also dem Kommenereignis, dass durch bspw. das Einstempeln erfasst wird.
        :param time: Zeitpunkt des Ereignisses
        :return: ComingBO
        """
        coming = ComingBO()
        coming.set_time(time)
        with ComingMapper() as mapper:
            return mapper.insert(coming)

    def get_coming_by_id(self, number):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um ein ComingBO mit bestimmter ID aus der Datenbank zu laden
        :return: ComingBO
        """
        with ComingMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle ComingBOs aus der Datenbank zu laden
    def get_all_comings(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um alle ComingBOs aus der Datenbank zu laden
        :return: Array mit ComingBOs
        """
        with ComingMapper() as mapper:
            return mapper.find_all()

    # Methode um ein ComingBOs zu updaten
    def save_coming(self, coming):
        with ComingMapper() as mapper:
            coming = mapper.update(coming)
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "coming_id", coming.get_id(), coming.get_type()
                )
                mapper.update(event)
                self.save_event_booking(event)

    def delete_coming(self, coming):
        """
        Author Khadidja Kebaili und Mihriban Dogan

        Löscht ein ComingBO inkl. der Eventbuchung (EventBookingBO) und der Buchung (BookingBO)
        :param coming: ComingBO
        """

        with EventMapper() as mapper:
            event = mapper.find_by_foreign_key_and_type(
                "coming_id", coming.get_id(), "coming")
        with EventBookingMapper() as mapper:
            eventbooking = mapper.find_by_event_id(event.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "eventBookingId", eventbooking.get_id(), "E")
            user = self.get_user_by_id(booking.get_user_id())

            workbookings = self.get_work_bookings_for_user(user)

        if len(workbookings) == 0:
            with EventMapper() as mapper:
                startevent = mapper.find_by_foreign_key_and_type(
                    "coming_id", coming.get_id(), coming.get_type()
                )
            with EventBookingMapper() as mapper:
                starteventbooking = mapper.find_by_event_id(
                    startevent.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "eventBookingId", starteventbooking.get_id(), "E"
                )

            with BookingMapper() as mapper:
                mapper.delete(booking)
            with EventBookingMapper() as mapper:
                mapper.delete(starteventbooking)
            with EventMapper() as mapper:
                mapper.delete(startevent)
            with ComingMapper() as mapper:
                mapper.delete(coming)
        else:
            for elem in workbookings:
                if coming.get_id() == elem.get_end_event():
                    return 400
                else:

                    with EventMapper() as mapper:
                        startevent = mapper.find_by_foreign_key_and_type(
                            "coming_id", coming.get_id(), coming.get_type()
                        )
                    with EventBookingMapper() as mapper:
                        starteventbooking = mapper.find_by_event_id(
                            startevent.get_id())
                    with BookingMapper() as mapper:
                        booking = mapper.find_booking_by_booking_subclass(
                            "eventBookingId", starteventbooking.get_id(), "E"
                        )

                    with BookingMapper() as mapper:
                        mapper.delete(booking)
                    with EventBookingMapper() as mapper:
                        mapper.delete(starteventbooking)
                    with EventMapper() as mapper:
                        mapper.delete(startevent)
                    with ComingMapper() as mapper:
                        mapper.delete(coming)

    def create_going(self, time):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

         Erstellung eines GoingBOs, also dem Kommenereignis, dass durch bspw. das Ausstempeln erfasst wird.
        :param time: Zeitpunkt des Ereignisses
        :return: GoingBO
        """
        going = GoingBO()
        going.set_time(time)
        with GoingMapper() as mapper:
            return mapper.insert(going)

    def get_going_by_id(self, number):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um ein GoingBO mit bestimmter ID aus der Datenbank zu laden
        :return: GoingBO
        """
        with GoingMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_goings(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um alle GoingBOs aus der Datenbank zu laden
        :return: Array mit GoingBOs
        """
        with GoingMapper() as mapper:
            return mapper.find_all()

    # Methode um ein GoingBO zu updaten
    def save_going(self, going):
        with GoingMapper() as mapper:
            going = mapper.update(going)
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "going_id", going.get_id(), going.get_type()
                )
                mapper.update(event)
                self.save_event_booking(event)

    def delete_going(self, going):
        """
        Author Khadidja Kebaili und Mihriban Dogan

        Löscht ein GoingBO inkl. der Eventbuchung (EventBookingBO) und der Buchung (BookingBO)
        :param going: GoingBO
        """
        with EventMapper() as mapper:
            event = mapper.find_by_foreign_key_and_type(
                "going_id", going.get_id(), "going")
        with EventBookingMapper() as mapper:
            eventbooking = mapper.find_by_event_id(event.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "eventBookingId", eventbooking.get_id(), "E")
            user = self.get_user_by_id(booking.get_user_id())

            workbookings = self.get_work_bookings_for_user(user)

            if len(workbookings) == 0:
                with EventMapper() as mapper:
                    endevent = mapper.find_by_foreign_key_and_type(
                        "going_id", going.get_id(), going.get_type()
                    )
                with EventBookingMapper() as mapper:
                    endeventbooking = mapper.find_by_event_id(
                        endevent.get_id())

                with BookingMapper() as mapper:
                    booking = mapper.find_booking_by_booking_subclass(
                        "eventBookingId", endeventbooking.get_id(), "E"
                    )

                with BookingMapper() as mapper:
                    mapper.delete(booking)

                with EventBookingMapper() as mapper:
                    mapper.delete(endeventbooking)
                with EventMapper() as mapper:
                    mapper.delete(endevent)
                with GoingMapper() as mapper:
                    mapper.delete(going)
            else:
                for elem in workbookings:
                    if going.get_id() == elem.get_start_event():
                        return 400
                    else:
                        with EventMapper() as mapper:
                            endevent = mapper.find_by_foreign_key_and_type(
                                "going_id", going.get_id(), going.get_type()
                            )
                        with EventBookingMapper() as mapper:
                            endeventbooking = mapper.find_by_event_id(
                                endevent.get_id())

                        with BookingMapper() as mapper:
                            booking = mapper.find_booking_by_booking_subclass(
                                "eventBookingId", endeventbooking.get_id(), "E"
                            )

                        with BookingMapper() as mapper:
                            mapper.delete(booking)

                        with EventBookingMapper() as mapper:
                            mapper.delete(endeventbooking)
                        with EventMapper() as mapper:
                            mapper.delete(endevent)
                        with GoingMapper() as mapper:
                            mapper.delete(going)

    def create_project_work_begin(self, time):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

         Erstellung eines ProjectWorkBeginBOs, also wenn ein Mitarbeiter mit der Projektarbeit beginnt
        :param time: Zeitpunkt des Ereignisses
        :return: ProjectWorkBeginBO
        """
        project_work_begin = ProjectWorkBeginBO()
        project_work_begin.set_time(time)
        with ProjectWorkBeginMapper() as mapper:
            return mapper.insert(project_work_begin)

    def get_project_work_begin_by_id(self, number):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um ein ProjectWorkBeginBO mit bestimmter ID aus der Datenbank zu laden
        :return: ProjectWorkBeginBO
        """
        with ProjectWorkBeginMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_project_work_begins(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um alle ProjectWorkBeginBOs aus der Datenbank zu laden
        :return: Array mit ProjectWorkBeginBOs
        """
        with ProjectWorkBeginMapper() as mapper:
            return mapper.find_all()

    # Methode um ein ProjectWorkBeginBOs zu updaten
    def save_project_work_begin(self, project_work_begin):
        with ProjectWorkBeginMapper() as mapper:
            mapper.update(project_work_begin)
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "project_work_begin_id", project_work_begin.get_id(), "projectWorkBegin")
                mapper.update(event)
                self.save_event_booking(event)

    # Methode um ein ProjectWorkBeginBO aus der Datenbank zu entfernen
    def delete_project_work_begin(self, project_work_begin):
        """
        Authors: Khadidja Kebaili und Mihriban Dogan

        Löscht ein ProjectWorkBeginBO inkl. der Eventbuchung (EventBookingBO) und der Buchung (BookingBO)
        :param project_work_begin: ProjectWorkBeginBO
        """
        with EventMapper() as mapper:
            startevent = mapper.find_by_foreign_key_and_type(
                "project_work_begin_id",
                project_work_begin.get_id(),
                project_work_begin.get_type(),
            )
        with EventBookingMapper() as mapper:
            starteventbooking = mapper.find_by_event_id(startevent.get_id())

        with EventBookingMapper() as mapper:
            mapper.delete(starteventbooking)
        with EventMapper() as mapper:
            mapper.delete(startevent)
        with ProjectWorkBeginMapper() as mapper:
            mapper.delete(project_work_begin)

    def create_project_work_end(self, time):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

         Erstellung eines ProjectWorkEndBOs, also wenn ein Mitarbeiter mit der Projektarbeit aufhört
        :param time: Zeitpunkt des Ereignisses
        :return: ProjectWorkEndBO
        """
        project_work_end = ProjectWorkEndBO()
        project_work_end.set_time(time)
        with ProjectWorkEndMapper() as mapper:
            return mapper.insert(project_work_end)

    def get_project_work_end_by_id(self, number):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um ein ProjectWorkEndBO mit bestimmter ID aus der Datenbank zu laden
        :return: ProjectWorkEndBO
        """
        with ProjectWorkEndMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle  aus der Datenbank zu laden
    def get_all_project_work_ends(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um alle ProjectWorkEndBOs aus der Datenbank zu laden
        :return: Array mit ProjectWorkEndBOs
        """
        with ProjectWorkEndMapper() as mapper:
            return mapper.find_all()

    # Methode um ein ProjectWorkEndBOs zu updaten
    def save_project_work_end(self, project_work_end):
        with ProjectWorkEndMapper() as mapper:
            mapper.update(project_work_end)
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "project_work_end_id",
                    project_work_end.get_id(),
                    project_work_end.get_type(),
                )
                mapper.update(event)
                self.save_event_booking(event)

    # Methode um ein ProjectWorkEndBO aus der Datenbank zu entfernen
    def delete_project_work_end(self, project_work_end):
        """
        Author Khadidja Kebaili und Mihriban Dogan

        Löscht ein ProjectWorkEndBO inkl. der Eventbuchung (EventBookingBO) und der Buchung (BookingBO)
        :param project_work_end: ProjectWorkEndBO
        """
        with EventMapper() as mapper:
            endevent = mapper.find_by_foreign_key_and_type(
                "project_work_end_id",
                project_work_end.get_id(),
                project_work_end.get_type(),
            )
        with EventBookingMapper() as mapper:
            endeventbooking = mapper.find_by_event_id(endevent.get_id())

        with EventBookingMapper() as mapper:
            mapper.delete(endeventbooking)
        with EventMapper() as mapper:
            mapper.delete(endevent)
        with VacationBeginMapper() as mapper:
            mapper.delete(project_work_end)

    def create_vacation_begin(self, time):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

         Erstellung eines VacationBeginBOs, also wenn ein Mitarbeiter seinen Urlaub antritt
        :param time: Zeitpunkt des Ereignisses
        :return: VacationBeginBO
        """
        vacation_begin = VacationBeginBO()
        vacation_begin.set_time(time)
        with VacationBeginMapper() as mapper:
            return mapper.insert(vacation_begin)

    def get_vacation_begin_by_id(self, number):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um ein VacationBeginBO mit bestimmter ID aus der Datenbank zu laden
        :return: VacationBeginBO
        """
        with VacationBeginMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle  aus der Datenbank zu laden
    def get_all_vacation_begins(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um alle VacationBeginBOs aus der Datenbank zu laden
        :return: Array mit VacationBeginBOs
        """
        with VacationBeginMapper() as mapper:
            return mapper.find_all()

    # Methode um ein VacationBeginBO zu updaten
    def save_vacation_begin(self, vacation_begin):
        with VacationBeginMapper() as mapper:
            mapper.update(vacation_begin)
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "vacation_begin_id",
                    vacation_begin.get_id(),
                    vacation_begin.get_type(),
                )
                mapper.update(event)
                self.save_event_booking(event)

    def delete_vacation_begin(self, vacation_begin):
        """
        Authors: Khadidja Kebaili und Mihriban Dogan

        Löscht ein VacationBeginBO inkl. der Eventbuchung (EventBookingBO) und der Buchung (BookingBO)
        :param vacation_begin: VacationBeginBO
        :return:
        """
        with EventMapper() as mapper:
            event = mapper.find_by_foreign_key_and_type(
                "vacation_begin_id", vacation_begin.get_id(), "vacationBegin")
        with EventBookingMapper() as mapper:
            eventbooking = mapper.find_by_event_id(event.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "eventBookingId", eventbooking.get_id(), "E")
            user = self.get_user_by_id(booking.get_user_id())

            workbookings = self.get_vacation_bookings_for_user(user)

            if len(workbookings) == 0:
                with EventMapper() as mapper:
                    startevent = mapper.find_by_foreign_key_and_type(
                        "vacation_begin_id", vacation_begin.get_id(), vacation_begin.get_type()
                    )
                with EventBookingMapper() as mapper:
                    starteventbooking = mapper.find_by_event_id(
                        startevent.get_id())
                with BookingMapper() as mapper:
                    booking = mapper.find_booking_by_booking_subclass(
                        "eventBookingId", starteventbooking.get_id(), "E"
                    )

                with BookingMapper() as mapper:
                    mapper.delete(booking)
                with EventBookingMapper() as mapper:
                    mapper.delete(starteventbooking)
                with EventMapper() as mapper:
                    mapper.delete(startevent)
                with VacationBeginMapper() as mapper:
                    mapper.delete(vacation_begin)
            else:
                for elem in workbookings:
                    if vacation_begin.get_id() == elem.get_start_event():
                        return 400
                    else:
                        with EventMapper() as mapper:
                            startevent = mapper.find_by_foreign_key_and_type(
                                "vacation_begin_id", vacation_begin.get_id(), vacation_begin.get_type()
                            )
                        with EventBookingMapper() as mapper:
                            starteventbooking = mapper.find_by_event_id(
                                startevent.get_id())
                        with BookingMapper() as mapper:
                            booking = mapper.find_booking_by_booking_subclass(
                                "eventBookingId", starteventbooking.get_id(), "E"
                            )

                        with BookingMapper() as mapper:
                            mapper.delete(booking)
                        with EventBookingMapper() as mapper:
                            mapper.delete(starteventbooking)
                        with EventMapper() as mapper:
                            mapper.delete(startevent)
                        with VacationBeginMapper() as mapper:
                            mapper.delete(vacation_begin)

    def create_vacation_end(self, time):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Erstellung eines VacationEndBOs, also wenn ein Mitarbeiter aus dem Urlaub kommt
        :param time: Zeitpunkt des Ereignisses
        :return: VacationEndBO
        """
        vacation_end = VacationEndBO()
        vacation_end.set_time(time)
        with VacationEndMapper() as mapper:
            return mapper.insert(vacation_end)

    def get_vacation_end_by_id(self, number):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um ein VacationEndBO  mit bestimmter ID aus der Datenbank zu laden
        :return: VacationEndBO
        """
        with VacationEndMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_vacation_ends(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um alle VacationEndBOs aus der Datenbank zu laden
        :return: Array mit VacationEndBOs
        """
        with VacationEndMapper() as mapper:
            return mapper.find_all()

    # Methode um ein VacationEndBO zu updaten
    def save_vacation_end(self, vacation_end):
        with VacationEndMapper() as mapper:
            mapper.update(vacation_end)

    # Methode um ein VacationEndBO aus der Datenbank zu entfernen
    def delete_vacation_end(self, vacation_end):
        """
        Author Khadidja Kebaili und Mihriban Dogan

        Löscht ein VacationEndBO inkl. der Eventbuchung (EventBookingBO) und der Buchung (BookingBO)
        :param vacation_end: VacationEndBO
        """
        with EventMapper() as mapper:
            event = mapper.find_by_foreign_key_and_type(
                "vacation_end_id", vacation_end.get_id(), "vacationEnd")
        with EventBookingMapper() as mapper:
            eventbooking = mapper.find_by_event_id(event.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "eventBookingId", eventbooking.get_id(), "E")
            user = self.get_user_by_id(booking.get_user_id())

            workbookings = self.get_vacation_bookings_for_user(user)

            if len(workbookings) == 0:
                with EventMapper() as mapper:
                    startevent = mapper.find_by_foreign_key_and_type(
                        "vacation_end_id", vacation_end.get_id(), vacation_end.get_type()
                    )
                with EventBookingMapper() as mapper:
                    starteventbooking = mapper.find_by_event_id(
                        startevent.get_id())
                with BookingMapper() as mapper:
                    booking = mapper.find_booking_by_booking_subclass(
                        "eventBookingId", starteventbooking.get_id(), "E"
                    )

                with BookingMapper() as mapper:
                    mapper.delete(booking)
                with EventBookingMapper() as mapper:
                    mapper.delete(starteventbooking)
                with EventMapper() as mapper:
                    mapper.delete(startevent)
                with VacationEndMapper() as mapper:
                    mapper.delete(vacation_end)
            else:
                for elem in workbookings:
                    if vacation_end.get_id() == elem.get_end_event():
                        return 400
                    else:
                        with EventMapper() as mapper:
                            startevent = mapper.find_by_foreign_key_and_type(
                                "vacation_end_id", vacation_end.get_id(), vacation_end.get_type()
                            )
                        with EventBookingMapper() as mapper:
                            starteventbooking = mapper.find_by_event_id(
                                startevent.get_id())
                        with BookingMapper() as mapper:
                            booking = mapper.find_booking_by_booking_subclass(
                                "eventBookingId", starteventbooking.get_id(), "E"
                            )

                        with BookingMapper() as mapper:
                            mapper.delete(booking)
                        with EventBookingMapper() as mapper:
                            mapper.delete(starteventbooking)
                        with EventMapper() as mapper:
                            mapper.delete(startevent)
                        with VacationEndMapper() as mapper:
                            mapper.delete(vacation_end)

    def create_illness_begin(self, time):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Erstellung eines IllnessBeginBOs, also der Beginn der Krankheit eines Mitarbeiters
        :param time: Zeitpunkt des Ereignisses
        :return: IllnessBeginBO
        """
        illness_begin = IllnessBeginBO()
        illness_begin.set_time(time)
        with IllnessBeginMapper() as mapper:
            return mapper.insert(illness_begin)

    def get_illness_begin_by_id(self, number):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um ein IllnessBeginBO   mit bestimmter ID aus der Datenbank zu laden
        :return: IllnessBeginBO
        """
        with IllnessBeginMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_illness_begins(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um alle IllnessBeginBOs aus der Datenbank zu laden
        :return: Array mit IllnessBeginBOs
        """
        with IllnessBeginMapper() as mapper:
            return mapper.find_all()

    # Methode um ein IllnessBeginBO zu updaten
    def save_illness_begin(self, illness_begin):
        with IllnessBeginMapper() as mapper:
            mapper.update(illness_begin)
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "illness_begin_id", illness_begin.get_id(), illness_begin.get_type()
                )
                mapper.update(event)
                self.save_event_booking(event)

    def delete_illness_begin(self, illness_begin):
        """
        Authors Khadidja Kebaili und Mihriban Dogan

        Löscht ein IllnessBeginBO inkl. der Eventbuchung (EventBookingBO) und der Buchung (BookingBO)
        :param illness_begin: IllnessBeginBO
        """
        with EventMapper() as mapper:
            event = mapper.find_by_foreign_key_and_type(
                "illness_begin_id", illness_begin.get_id(), "illnessBegin")
        with EventBookingMapper() as mapper:
            eventbooking = mapper.find_by_event_id(event.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "eventBookingId", eventbooking.get_id(), "E")
            user = self.get_user_by_id(booking.get_user_id())

            workbookings = self.get_illness_bookings_for_user(user)

            if len(workbookings) == 0:
                with EventMapper() as mapper:
                    startevent = mapper.find_by_foreign_key_and_type(
                        "illness_begin_id", illness_begin.get_id(), illness_begin.get_type()
                    )
                with EventBookingMapper() as mapper:
                    starteventbooking = mapper.find_by_event_id(
                        startevent.get_id())
                with BookingMapper() as mapper:
                    booking = mapper.find_booking_by_booking_subclass(
                        "eventBookingId", starteventbooking.get_id(), "E"
                    )

                with BookingMapper() as mapper:
                    mapper.delete(booking)
                with EventBookingMapper() as mapper:
                    mapper.delete(starteventbooking)
                with EventMapper() as mapper:
                    mapper.delete(startevent)
                with IllnessBeginMapper() as mapper:
                    mapper.delete(illness_begin)
            else:
                for elem in workbookings:
                    if illness_begin.get_id() == elem.get_start_event():
                        return 400
                    else:
                        with EventMapper() as mapper:
                            startevent = mapper.find_by_foreign_key_and_type(
                                "illness_begin_id", illness_begin.get_id(), illness_begin.get_type()
                            )
                        with EventBookingMapper() as mapper:
                            starteventbooking = mapper.find_by_event_id(
                                startevent.get_id())
                        with BookingMapper() as mapper:
                            booking = mapper.find_booking_by_booking_subclass(
                                "eventBookingId", starteventbooking.get_id(), "E"
                            )

                        with BookingMapper() as mapper:
                            mapper.delete(booking)
                        with EventBookingMapper() as mapper:
                            mapper.delete(starteventbooking)
                        with EventMapper() as mapper:
                            mapper.delete(startevent)
                        with IllnessBeginMapper() as mapper:
                            mapper.delete(illness_begin)

    def create_illness_end(self, time):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Erstellung eines IllnessEndBOs, also das Ende der Krankheit eines Mitarbeiters
        :param time: Zeitpunkt des Ereignisses
        :return: IllnessEndBO
        """
        illness_end = IllnessEndBO()
        illness_end.set_time(time)
        with IllnessEndMapper() as mapper:
            return mapper.insert(illness_end)

    def get_illness_end_by_id(self, number):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um ein IllnessEndBO mit bestimmter ID aus der Datenbank zu laden
        :return: IllnessEndBO
        """
        with IllnessEndMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_illness_end(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um alle IllnessEndBOs aus der Datenbank zu laden
        :return: Array mit IllnessEndBOs
        """
        with IllnessEndMapper() as mapper:
            return mapper.find_all()

    # Methode um ein IllnessEndBO zu updaten
    def save_illness_end(self, illness_end):
        with IllnessEndMapper() as mapper:
            mapper.update(illness_end)
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "illness_end_id", illness_end.get_id(), illness_end.get_type()
                )
                mapper.update(event)
                self.save_event_booking(event)

    def delete_illness_end(self, illness_end):
        """
        Author Khadidja Kebaili und Mihriban Dogan

        Löscht ein VacationEndBO inkl. der Eventbuchung (EventBookingBO) und der Buchung (BookingBO)
        :param illness_end: IllnessEndBO
        """
        with EventMapper() as mapper:
            event = mapper.find_by_foreign_key_and_type(
                "illness_end_id", illness_end.get_id(), "illnessEnd")
        with EventBookingMapper() as mapper:
            eventbooking = mapper.find_by_event_id(event.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "eventBookingId", eventbooking.get_id(), "E")
            user = self.get_user_by_id(booking.get_user_id())

            workbookings = self.get_illness_bookings_for_user(user)

        if len(workbookings) == 0:
            with EventMapper() as mapper:
                endevent = mapper.find_by_foreign_key_and_type(
                    "illness_end_id", illness_end.get_id(), illness_end.get_type()
                )
            with EventBookingMapper() as mapper:
                endeventbooking = mapper.find_by_event_id(
                    endevent.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "eventBookingId", endeventbooking.get_id(), "E"
                )
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with EventBookingMapper() as mapper:
                mapper.delete(endeventbooking)
            with EventMapper() as mapper:
                mapper.delete(endevent)
            with IllnessEndMapper() as mapper:
                mapper.delete(illness_end)
        else:
            for elem in workbookings:
                if illness_end.get_id() == elem.get_end_event():
                    return 400
                else:
                    with EventMapper() as mapper:
                        endevent = mapper.find_by_foreign_key_and_type(
                            "illness_end_id", illness_end.get_id(), illness_end.get_type()
                        )
                    with EventBookingMapper() as mapper:
                        endeventbooking = mapper.find_by_event_id(
                            endevent.get_id())
                    with BookingMapper() as mapper:
                        booking = mapper.find_booking_by_booking_subclass(
                            "eventBookingId", endeventbooking.get_id(), "E"
                        )
                    with BookingMapper() as mapper:
                        mapper.delete(booking)
                    with EventBookingMapper() as mapper:
                        mapper.delete(endeventbooking)
                    with EventMapper() as mapper:
                        mapper.delete(endevent)
                    with IllnessEndMapper() as mapper:
                        mapper.delete(illness_end)

    def create_flex_day_start(self, time):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Erstellung eines FlexDayStartBOs, also der Beginn des Gleittags eines Mitarbeiters.
        :param time: Zeitpunkt des Ereignisses
        :return: FlexDayStartBO
        """
        flex_day_start = FlexDayStartBO()
        flex_day_start.set_time(time)
        with FlexDayStartMapper() as mapper:
            return mapper.insert(flex_day_start)

    def get_flex_day_start_by_id(self, number):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um ein FlexDayStartBO mit bestimmter ID aus der Datenbank zu laden
        :return: FlexDayStartBO
        """
        with FlexDayStartMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_flex_day_starts(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um alle FlexDayStartBOs  aus der Datenbank zu laden
        :return: Array mit FlexDayStartBOs IllnessBeginBOs
        """
        with FlexDayStartMapper() as mapper:
            return mapper.find_all()

    # Methode um ein FlexDayStartBO zu updaten
    def save_flex_day_start(self, flex_day_start):
        with FlexDayStartMapper() as mapper:
            mapper.update(flex_day_start)
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "flex_day_start_id",
                    flex_day_start.get_id(),
                    flex_day_start.get_type(),
                )
                print(flex_day_start.get_id())
                mapper.update(event)
                self.save_event_booking(event)

    def delete_flex_day_start(self, flex_day_start):
        """
        Author Khadidja Kebaili und Mihriban Dogan

        Löscht ein FlexDayStartBO inkl. der Eventbuchung (EventBookingBO) und der Buchung (BookingBO)
        :param flex_day_start: FlexDayStartBO
        """
        with EventMapper() as mapper:
            startevent = mapper.find_by_foreign_key_and_type(
                "flex_day_start_id", flex_day_start.get_id(), flex_day_start.get_type()
            )
        with EventBookingMapper() as mapper:
            starteventbooking = mapper.find_by_event_id(startevent.get_id())

        with EventBookingMapper() as mapper:
            mapper.delete(starteventbooking)
        with EventMapper() as mapper:
            mapper.delete(startevent)
        with FlexDayMapper() as mapper:
            mapper.delete(flex_day_start)

    def create_flex_day_end(self, time):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Erstellung eines FlexDayEndBOs, also das Ende der Gleittage eines Mitarbeiters
        :param time: Zeitpunkt des Ereignisses
        :return: FlexDayEndBO
        """
        flex_day_end = FlexDayEndBO()
        flex_day_end.set_time(time)
        with FlexDayEndMapper() as mapper:
            return mapper.insert(flex_day_end)

    def get_flex_day_end_by_id(self, number):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um ein FlexDayEndBO mit bestimmter ID aus der Datenbank zu laden
        :return: FlexDayEndBO
        """
        with FlexDayEndMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_flex_day_end(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um alle FlexDayEndBOs aus der Datenbank zu laden
        :return: Array mit FlexDayEndBOs
        """
        with FlexDayEndMapper() as mapper:
            return mapper.find_all()

    # Methode um ein FlexDayEndBO zu updaten
    def save_flex_day_end(self, flex_day_end):
        with FlexDayEndMapper() as mapper:
            mapper.update(flex_day_end)
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "flex_day_end_id", flex_day_end.get_id(), flex_day_end.get_type()
                )
                mapper.update(event)
                self.save_event_booking(event)

    # Methode um ein FlexDayEndBO aus der Datenbank zu entfernen
    def delete_flex_day_end(self, flex_day_end):
        """
        Author Khadidja Kebaili und Mihriban Dogan

        Löscht ein FlexEndBO inkl. der Eventbuchung (EventBookingBO) und der Buchung (BookingBO)
        :param flex_day_end: FlexEndBO
        :return:
        """
        with EventMapper() as mapper:
            endevent = mapper.find_by_foreign_key_and_type(
                "flex_day_end_id", flex_day_end.get_id(), flex_day_end.get_type()
            )
        with EventBookingMapper() as mapper:
            endeventbooking = mapper.find_by_event_id(endevent.get_id())

        with EventBookingMapper() as mapper:
            mapper.delete(endeventbooking)
        with EventMapper() as mapper:
            mapper.delete(endevent)
        with FlexDayEndMapper() as mapper:
            mapper.delete(flex_day_end)

    def create_break_begin(self, time):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Erstellung eines BreakBeginBOs, also des Pausenbegins eines Mitarbeiters.
        :param time: Zeitpunkt des Ereignisses
        :return: BreakBeginBO
        """
        break_begin = BreakBeginBO()
        break_begin.set_time(time)
        with BreakBeginMapper() as mapper:
            return mapper.insert(break_begin)

    def get_break_begin_by_id(self, number):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um ein BreakBeginBO mit bestimmter ID aus der Datenbank zu laden
        :return: BreakBeginBO
        """
        with BreakBeginMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_break_begins(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um alle BreakBeginBOs aus der Datenbank zu laden
        :return: Array mit BreakBeginBOs
        """
        with BreakBeginMapper() as mapper:
            return mapper.find_all()

    # Methode um ein BreakBeginBO zu updaten
    def save_break_begin(self, break_begin):
        with BreakBeginMapper() as mapper:
            mapper.update(break_begin)
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "break_begin_id", break_begin.get_id(), break_begin.get_type()
                )
                mapper.update(event)
                self.save_event_booking(event)

    # Methode um ein BreakBeginBO aus der Datenbank zu entfernen
    def delete_break_begin(self, break_begin):
        """
        Author Khadidja Kebaili und Mihriban Dogan

        Löscht ein BreakBeginBO inkl. der Eventbuchung (EventBookingBO) und der Buchung (BookingBO)
        :param break_begin: BreakBeginBO
        :return:
        """
        with BreakBeginMapper() as mapper:
            mapper.delete(break_begin)

    def create_break_end(self, time):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Erstellung eines BreakEndBOs, also das Ende der Krankheit eines Mitarbeiters
        :param time: Zeitpunkt des Ereignisses
        :return: BreakBeginBO
        """
        break_end = BreakEndBO()
        break_end.set_time(time)
        with BreakEndMapper() as mapper:
            return mapper.insert(break_end)

    # Methode um ein BreakEndBO mit bestimmter ID aus der Datenbank zu laden

    def get_break_end_by_id(self, number):
        with BreakEndMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_break_ends(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Methode um alle BreakEndBOs  aus der Datenbank zu laden
        :return: Array mit BreakEndBOs
        """
        with BreakEndMapper() as mapper:
            return mapper.find_all()

    # Methode um ein BreakEndBO zu updaten
    def save_break_end(self, break_end):
        with BreakEndMapper() as mapper:
            mapper.update(break_end)
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "break_end_id", break_end.get_id(), break_end.get_type()
                )
                mapper.update(event)
                self.save_event_booking(event)

    # Methode um ein BreakEndBO aus der Datenbank zu entfernen
    def delete_breakEnd(self, break_end):
        """
        Author Khadidja Kebaili und Mihriban Dogan

        Löscht ein BreakEndBO inkl. der Eventbuchung (EventBookingBO) und der Buchung (BookingBO)
        :param breakEnd: BreakEndBO
        :return:
        """
        with BreakEndMapper() as mapper:
            mapper.delete(break_end)

    # Support-Funktion
    def get_all_event_subclasses(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Alle Subklassen der Klasse EventBO
        :return: Array mit allen Event-Subklassen
        """
        events = [
            self.get_all_break_ends(),
            self.get_all_break_begins(),
            self.get_all_project_work_begins(),
            self.get_all_project_work_ends(),
            self.get_all_vacation_begins(),
            self.get_all_vacation_ends(),
            self.get_all_illness_begins(),
            self.get_all_illness_end(),
            self.get_all_comings(),
            self.get_all_goings(),
        ]
        return events

    """
    Timeinterval Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """

    def get_all_timeintervals(self):
        # alle Timeintervalle holen
        with TimeIntervalMapper() as mapper:
            return mapper.find_all()

    def get_timeinterval_by_id(self, id):
        # Timeinterval mit gegebener Id holen
        with TimeIntervalMapper() as mapper:
            return mapper.find_by_key(id)

    def create_timeinterval(self, type, break_id, illness_id, project_duration_id, project_work_id, vacation_id,
                            flexday_id, work_id):
        # neues TimeintervalBO erstellen
        timeinterval = TimeIntervalBO()
        timeinterval.set_type(type)
        timeinterval.set_break_id(break_id)
        timeinterval.set_illness_id(illness_id)
        timeinterval.set_project_duration_id(project_duration_id)
        timeinterval.set_project_work_id(project_work_id)
        timeinterval.set_vacation_id(vacation_id)
        timeinterval.set_flex_day_id(flexday_id)
        timeinterval.set_work_id(work_id)

        with TimeIntervalMapper() as mapper:
            return mapper.insert(timeinterval)

    def save_timeinterval(self, timeinterval):
        # Änderungen im gegebenen TimeintervalBO abspeichern
        with TimeIntervalMapper() as mapper:
            return mapper.update(timeinterval)

    def delete_timeinterval(self, timeinterval):
        # löscht ein Timeinterval
        with TimeIntervalMapper() as mapper:
            mapper.delete(timeinterval)

    def get_timeinterval_by_type(self, type):
        # holt Timeintervalle mit gegebenen Type
        with TimeIntervalMapper() as mapper:
            mapper.find_by_type(type)

    def get_subclass_timeinterval_by_timeinterval(self, timeinterval):
        # @author Mihriban Dogan (https://github.com/mihriban-dogan)
        # holt die Subklassen zu den zugehörigen Timeinterval
        type = timeinterval.get_type()
        if type == 'Break':
            res = self.get_break_by_id(timeinterval.get_break_id())
        if type == 'Illness':
            res = self.get_illness_by_id(timeinterval.get_illness_id())
        if type == 'ProjectDuration':
            res = self.get_project_duration_by_id(
                timeinterval.get_project_duration_id())
        if type == 'ProjectWork':
            res = self.get_project_work_by_id(
                timeinterval.get_project_work_id())
        if type == 'Vacation':
            res = self.get_vacation_by_id(timeinterval.get_vacation_id())
            with VacationMapper() as mapper:
                mapper.find_by_key()
        if type == 'Work':
            res = self.get_work_by_id(timeinterval.get_work_id())
        return res

    """
    Break Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """

    def get_all_breaks(self):
        # alle Breaks holen
        with BreakMapper() as mapper:
            return mapper.find_all()

    def get_break_by_id(self, id):
        # BreakBO mit gegebener Id holen
        with BreakMapper() as mapper:
            return mapper.find_by_key(id)

    def create_break(self, start, end, s_event, e_event):
        # BreakBO erstellen
        break_obj = BreakBO()
        break_obj.set_start(start)
        break_obj.set_end(end)
        break_obj.set_start_event(s_event)
        break_obj.set_end_event(e_event)
        break_obj.set_type("Break")

        with BreakMapper() as mapper:
            return mapper.insert(break_obj)

    def create_break_with_interval(self, start, end, s_event, e_event):
        # BreakBO erstellen        
        break_obj = BreakBO()
        break_obj.set_start(start)
        break_obj.set_end(end)
        break_obj.set_start_event(s_event)
        break_obj.set_end_event(e_event)
        break_obj.set_type("Break")

        with BreakMapper() as mapper:
            return mapper.insert(break_obj)

    def save_break(self, break_obj):
        # Änderung in Break abspeichern
        with BreakMapper() as mapper:
            mapper.update(break_obj)
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "breakId", break_obj.get_id(), break_obj.get_type())
                print(timeinterval)
                mapper.update(timeinterval)
                self.save_time_interval_booking(timeinterval)

    def delete_break(self, break_obj):
        # @author Mihriban Dogan (https://github.com/mihriban-dogan)
        # BreakBO löschen -> zugehörige Subklassen müssen ebenfalls gelöscht werden
        with BreakBeginMapper() as mapper:
            break_begin = mapper.find_by_key(
                break_obj.get_start_event())
        with BreakEndMapper() as mapper:
            break_end = mapper.find_by_key(
                break_obj.get_end_event())
        with EventMapper() as mapper:
            startevent = mapper.find_by_foreign_key_and_type(
                "break_begin_id", break_begin.get_id(), break_begin.get_type())
        with EventMapper() as mapper:
            endevent = mapper.find_by_foreign_key_and_type(
                "break_end_id", break_end.get_id(), break_end.get_type())
        with EventBookingMapper() as mapper:
            starteventbooking = mapper.find_by_event_id(startevent.get_id())
        with EventBookingMapper() as mapper:
            endeventbooking = mapper.find_by_event_id(endevent.get_id())
        with TimeIntervalMapper() as mapper:
            timeinterval = mapper.find_by_foreign_key_and_type(
                "breakId", break_obj.get_id(), break_obj.get_type())
        with TimeIntervalBookingMapper() as mapper:
            timeintervalbooking = mapper.find_by_timeinterval_id(
                timeinterval.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")

        with BookingMapper() as mapper:
            mapper.delete(booking)
        with TimeIntervalBookingMapper() as mapper:
            mapper.delete(timeintervalbooking)
        with TimeIntervalMapper() as mapper:
            mapper.delete(timeinterval)
        with BreakMapper() as mapper:
            mapper.delete(break_obj)
        with EventBookingMapper() as mapper:
            mapper.delete(starteventbooking)
        with EventBookingMapper() as mapper:
            mapper.delete(endeventbooking)
        with EventMapper() as mapper:
            mapper.delete(startevent)
        with EventMapper() as mapper:
            mapper.delete(endevent)
        with BreakBeginMapper() as mapper:
            mapper.delete(break_begin)
        with BreakEndMapper() as mapper:
            mapper.delete(break_end)

    def get_breaks_by_date(self, date):
        # Breaks an gegebenen Date holen
        with BreakMapper() as mapper:
            return mapper.find_by_date(date)

    def get_breaks_by_time_period(self, startdate, enddate):
        # Breaks im gegebenen Zeitinterval holen
        with BreakMapper() as mapper:
            return mapper.find_by_time_period(startdate, enddate)

    """
    Illness Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """

    
    def get_all_illnesses(self):
        # alle IllnessBO holen
        with IllnessMapper() as mapper:
            return mapper.find_all()
    
    def get_illness_by_id(self, id):
        # IllnessBO mit gegebener id holen
        with IllnessMapper() as mapper:
            return mapper.find_by_key(id)

    def create_illness(self, start, end, startevent, endevent):
        # IllnessBO erstellen
        illness = IllnessBO()
        illness.set_start(start)
        illness.set_end(end)
        illness.set_start_event(startevent)
        illness.set_end_event(endevent)
        illness.set_type("Illness")

        with IllnessMapper() as mapper:
            return mapper.insert(illness)

    
    def save_illness(self, illness):
        # Änderungen in IllnessBO erstellen
        with IllnessMapper() as mapper:
            mapper.update(illness)
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "illnessId", illness.get_id(), illness.get_type())
                print(timeinterval)
                mapper.update(timeinterval)
                self.save_time_interval_booking(timeinterval)

    def delete_illness(self, illness):
        # @author Mihriban Dogan (https://github.com/mihriban-dogan)
        # IllnessBO löschen
        if not ((illness.get_start_event() and illness.get_end_event()) == None):
            with IllnessBeginMapper() as mapper:
                illness_begin = mapper.find_by_key(
                    illness.get_start_event())
            with IllnessEndMapper() as mapper:
                illness_end = mapper.find_by_key(
                    illness.get_end_event())
            with EventMapper() as mapper:
                startevent = mapper.find_by_foreign_key_and_type(
                    "illness_begin_id", illness_begin.get_id(), illness_begin.get_type())
            with EventMapper() as mapper:
                endevent = mapper.find_by_foreign_key_and_type(
                    "illness_end_id", illness_end.get_id(), illness_end.get_type())
            with EventBookingMapper() as mapper:
                starteventbooking = mapper.find_by_event_id(
                    startevent.get_id())
            with EventBookingMapper() as mapper:
                endeventbooking = mapper.find_by_event_id(endevent.get_id())
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "illnessId", illness.get_id(), illness.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                starteventeventbooking = mapper.find_booking_by_booking_subclass(
                    "eventBookingId", starteventbooking.get_id(), "E")
            with BookingMapper() as mapper:
                endeventeventbooking = mapper.find_booking_by_booking_subclass(
                    "eventBookingId", endeventbooking.get_id(), "E")

            with BookingMapper() as mapper:
                mapper.delete(booking)
            with BookingMapper() as mapper:
                mapper.delete(starteventeventbooking)
            with BookingMapper() as mapper:
                mapper.delete(endeventeventbooking)
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with IllnessMapper() as mapper:
                mapper.delete(illness)
            with EventBookingMapper() as mapper:
                mapper.delete(starteventbooking)
            with EventBookingMapper() as mapper:
                mapper.delete(endeventbooking)
            with EventMapper() as mapper:
                mapper.delete(startevent)
            with EventMapper() as mapper:
                mapper.delete(endevent)
            with IllnessBeginMapper() as mapper:
                mapper.delete(illness_begin)
            with IllnessEndMapper() as mapper:
                mapper.delete(illness_end)
        elif (illness.get_start_event() and illness.get_end_event()) == None:
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "illnessId", illness.get_id(), illness.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with IllnessMapper() as mapper:
                mapper.delete(illness)
        elif not (illness.get_start_event() == None):
            with IllnessBeginMapper() as mapper:
                illness_begin = mapper.find_by_key(
                    illness.get_start_event())
            with EventMapper() as mapper:
                startevent = mapper.find_by_foreign_key_and_type(
                    "illness_begin_id", illness_begin.get_id(), illness_begin.get_type())
            with EventBookingMapper() as mapper:
                starteventbooking = mapper.find_by_event_id(
                    startevent.get_id())
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "illnessId", illness.get_id(), illness.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with IllnessMapper() as mapper:
                mapper.delete(illness)
            with EventBookingMapper() as mapper:
                mapper.delete(starteventbooking)
            with EventMapper() as mapper:
                mapper.delete(startevent)
            with IllnessBeginMapper() as mapper:
                mapper.delete(illness_begin)
        elif not (illness.get_end_event() == None):
            with IllnessEndMapper() as mapper:
                illness_end = mapper.find_by_key(
                    illness.get_end_event())
            with EventMapper() as mapper:
                endevent = mapper.find_by_foreign_key_and_type(
                    "illness_end_id", illness_end.get_id(), illness_end.get_type())
            with EventBookingMapper() as mapper:
                endeventbooking = mapper.find_by_event_id(endevent.get_id())
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "illnessId", illness.get_id(), illness.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with IllnessMapper() as mapper:
                mapper.delete(illness)
            with EventBookingMapper() as mapper:
                mapper.delete(endeventbooking)
            with EventMapper() as mapper:
                mapper.delete(endevent)
            with IllnessEndMapper() as mapper:
                mapper.delete(illness_end)

    def get_illnesses_by_date(self, date):
        # IllnessBO mit gegebenen Date holen
        with IllnessMapper() as mapper:
            return mapper.find_by_date(date)

    def get_illnesses_by_time_period(self, startdate, enddate):
        # IllnessBO aus gegebenen Zeitraum holen
        with IllnessMapper() as mapper:
            return mapper.find_by_time_period(startdate, enddate)

    """
    Vacation Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """

    def get_all_vacations(self):
        # alle VacationBO holen
        with VacationMapper() as mapper:
            return mapper.find_all()

    def get_vacation_by_id(self, id):
        # VacationBO mit gegebener id holen
        with VacationMapper() as mapper:
            return mapper.find_by_key(id)

    def create_vacation(self, start, end, startevent, endevent, type):
        # VacationBO erstellen
        vacation_obj = VacationBO()
        vacation_obj.set_start(start)
        vacation_obj.set_end(end)
        vacation_obj.set_start_event(startevent)
        vacation_obj.set_end_event(endevent)
        vacation_obj.set_type(type)

        with VacationMapper() as mapper:
            return mapper.insert(vacation_obj)

    
    def save_vacation(self, vacation_obj):
        # VacationBO Änderungen speichern
        with VacationMapper() as mapper:
            mapper.update(vacation_obj)
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "vacationId", vacation_obj.get_id(), vacation_obj.get_type())
                print(timeinterval)
                mapper.update(timeinterval)
                self.save_time_interval_booking(timeinterval)


    def delete_vacation(self, vacation_obj):
        # @author Mihriban Dogan (https://github.com/mihriban-dogan)
        # VacationBO löschen
        if not ((vacation_obj.get_start_event() and vacation_obj.get_end_event()) == None):
            with VacationBeginMapper() as mapper:
                vacation_begin = mapper.find_by_key(
                    vacation_obj.get_start_event())
            with VacationEndMapper() as mapper:
                vacation_end = mapper.find_by_key(
                    vacation_obj.get_end_event())
            with EventMapper() as mapper:
                startevent = mapper.find_by_foreign_key_and_type(
                    "vacation_begin_id", vacation_begin.get_id(), vacation_begin.get_type())
            with EventMapper() as mapper:
                endevent = mapper.find_by_foreign_key_and_type(
                    "vacation_end_id", vacation_end.get_id(), vacation_end.get_type())
            with EventBookingMapper() as mapper:
                starteventbooking = mapper.find_by_event_id(
                    startevent.get_id())
            with EventBookingMapper() as mapper:
                endeventbooking = mapper.find_by_event_id(endevent.get_id())
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "vacationId", vacation_obj.get_id(), vacation_obj.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                starteventeventbooking = mapper.find_booking_by_booking_subclass(
                    "eventBookingId", starteventbooking.get_id(), "E")
            with BookingMapper() as mapper:
                endeventeventbooking = mapper.find_booking_by_booking_subclass(
                    "eventBookingId", endeventbooking.get_id(), "E")

            with BookingMapper() as mapper:
                mapper.delete(booking)
            with BookingMapper() as mapper:
                mapper.delete(starteventeventbooking)
            with BookingMapper() as mapper:
                mapper.delete(endeventeventbooking)

            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with VacationMapper() as mapper:
                mapper.delete(vacation_obj)
            with EventBookingMapper() as mapper:
                mapper.delete(starteventbooking)
            with EventBookingMapper() as mapper:
                mapper.delete(endeventbooking)
            with EventMapper() as mapper:
                mapper.delete(startevent)
            with EventMapper() as mapper:
                mapper.delete(endevent)
            with VacationBeginMapper() as mapper:
                mapper.delete(vacation_begin)
            with VacationEndMapper() as mapper:
                mapper.delete(vacation_end)
        elif (vacation_obj.get_start_event() and vacation_obj.get_end_event()) == None:
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "vacationId", vacation_obj.get_id(), vacation_obj.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with VacationMapper() as mapper:
                mapper.delete(vacation_obj)
        elif not (vacation_obj.get_start_event() == None):
            with VacationBeginMapper() as mapper:
                vacation_begin = mapper.find_by_key(
                    vacation_obj.get_start_event())
            with EventMapper() as mapper:
                startevent = mapper.find_by_foreign_key_and_type(
                    "vacation_begin_id", vacation_begin.get_id(), vacation_begin.get_type())
            with EventBookingMapper() as mapper:
                starteventbooking = mapper.find_by_event_id(
                    startevent.get_id())
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "vacationId", vacation_obj.get_id(), vacation_obj.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with VacationMapper() as mapper:
                mapper.delete(vacation_obj)
            with EventBookingMapper() as mapper:
                mapper.delete(starteventbooking)
            with EventMapper() as mapper:
                mapper.delete(startevent)
            with VacationBeginMapper() as mapper:
                mapper.delete(vacation_begin)
        elif not (vacation_obj.get_end_event() == None):
            with VacationEndMapper() as mapper:
                vacation_end = mapper.find_by_key(
                    vacation_obj.get_end_event())
            with EventMapper() as mapper:
                endevent = mapper.find_by_foreign_key_and_type(
                    "vacation_end_id", vacation_end.get_id(), vacation_end.get_type())
            with EventBookingMapper() as mapper:
                endeventbooking = mapper.find_by_event_id(endevent.get_id())
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "vacationId", vacation_obj.get_id(), vacation_obj.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with VacationMapper() as mapper:
                mapper.delete(vacation_obj)
            with EventBookingMapper() as mapper:
                mapper.delete(endeventbooking)
            with EventMapper() as mapper:
                mapper.delete(endevent)
            with VacationEndMapper() as mapper:
                mapper.delete(vacation_end)

    def get_vacations_by_date(self, date):
        # VacationBO mit gegebenen Date
        with VacationMapper() as mapper:
            return mapper.find_by_date(date)
    
    def get_vacations_by_time_period(self, startdate, enddate):
        # VacationBO innerhalb gegebenen Zeitraum
        with VacationMapper() as mapper:
            return mapper.find_by_time_period(startdate, enddate)

    """
    Work Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """
    
    def get_all_works(self):
        # alle WorkBO holen
        with WorkMapper() as mapper:
            return mapper.find_all()

    
    def get_work_by_id(self, id):
        # WorkBO mit gegebener Id holen
        with WorkMapper() as mapper:
            return mapper.find_by_key(id)

    
    def create_work(self, start, end, startevent, endevent, type):
        # WorkBO erstellen
        work_obj = WorkBO()
        work_obj.set_start(start)
        work_obj.set_end(end)
        work_obj.set_start_event(startevent)
        work_obj.set_end_event(endevent)
        work_obj.set_type(type)

        with WorkMapper() as mapper:
            return mapper.insert(work_obj)

    
    def save_work(self, work_obj):
        # Änderungen in WorkBO speichern
        with WorkMapper() as mapper:
            work = mapper.update(work_obj)
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "workId", work.get_id(), work.get_type())
                mapper.update(timeinterval)
                self.save_time_interval_booking(timeinterval)


    def delete_work(self, work_obj):
        # @author Mihriban Dogan (https://github.com/mihriban-dogan)
        # WorkBO löschen
        if not ((work_obj.get_start_event() and work_obj.get_end_event()) == None):
            with ComingMapper() as mapper:
                coming = mapper.find_by_key(
                    work_obj.get_start_event())
            with GoingMapper() as mapper:
                going = mapper.find_by_key(
                    work_obj.get_end_event())
            with EventMapper() as mapper:
                startevent = mapper.find_by_foreign_key_and_type(
                    "coming_id", coming.get_id(), "coming")
            with EventMapper() as mapper:
                endevent = mapper.find_by_foreign_key_and_type(
                    "going_id", going.get_id(), "going")
            with EventBookingMapper() as mapper:
                starteventbooking = mapper.find_by_event_id(
                    startevent.get_id())
            with EventBookingMapper() as mapper:
                endeventbooking = mapper.find_by_event_id(endevent.get_id())
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "workId", work_obj.get_id(), work_obj.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "timeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                starteventeventbooking = mapper.find_booking_by_booking_subclass(
                    "eventBookingId", starteventbooking.get_id(), "E")
            with BookingMapper() as mapper:
                endeventeventbooking = mapper.find_booking_by_booking_subclass(
                    "eventBookingId", endeventbooking.get_id(), "E")

            with BookingMapper() as mapper:
                mapper.delete(booking)
            with BookingMapper() as mapper:
                mapper.delete(starteventeventbooking)
            with BookingMapper() as mapper:
                mapper.delete(endeventeventbooking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with WorkMapper() as mapper:
                mapper.delete(work_obj)
            with EventBookingMapper() as mapper:
                mapper.delete(starteventbooking)
            with EventBookingMapper() as mapper:
                mapper.delete(endeventbooking)
            with EventMapper() as mapper:
                mapper.delete(startevent)
            with EventMapper() as mapper:
                mapper.delete(endevent)
            with ComingMapper() as mapper:
                mapper.delete(coming)
            with GoingMapper() as mapper:
                mapper.delete(going)
        elif (work_obj.get_start_event() and work_obj.get_end_event()) == None:
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "workId", work_obj.get_id(), work_obj.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with WorkMapper() as mapper:
                mapper.delete(work_obj)
        elif not (work_obj.get_start_event() == None):
            with ComingMapper() as mapper:
                coming = mapper.find_by_key(
                    work_obj.get_start_event())
            with EventMapper() as mapper:
                startevent = mapper.find_by_foreign_key_and_type(
                    "coming_id", coming.get_id(), coming.get_type())
            with EventBookingMapper() as mapper:
                starteventbooking = mapper.find_by_event_id(
                    startevent.get_id())
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "workId", work_obj.get_id(), work_obj.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with WorkMapper() as mapper:
                mapper.delete(work_obj)
            with EventBookingMapper() as mapper:
                mapper.delete(starteventbooking)
            with EventMapper() as mapper:
                mapper.delete(startevent)
            with ComingMapper() as mapper:
                mapper.delete(coming)
        elif not (work_obj.get_end_event() == None):
            with WorkMapper() as mapper:
                going = mapper.find_by_key(
                    work_obj.get_end_event())
            with EventMapper() as mapper:
                endevent = mapper.find_by_foreign_key_and_type(
                    "going_id", going.get_id(), going.get_type())
            with EventBookingMapper() as mapper:
                endeventbooking = mapper.find_by_event_id(endevent.get_id())
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "workId", work_obj.get_id(), work_obj.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with WorkMapper() as mapper:
                mapper.delete(work_obj)
            with EventBookingMapper() as mapper:
                mapper.delete(endeventbooking)
            with EventMapper() as mapper:
                mapper.delete(endevent)
            with WorkMapper() as mapper:
                mapper.delete(going)
    
    def get_works_by_date(self, date):
        # WorkBO mit gegebenen Date holen
        with WorkMapper() as mapper:
            return mapper.find_by_date(date)

    def get_works_by_time_period(self, startdate, enddate):
        # WorkBO aus gegebenen Zeitraum holen
        with WorkMapper() as mapper:
            return mapper.find_by_time_period(startdate, enddate)

    """
    FlexDay Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """

    def get_all_flex_days(self):
        # alle FlexDayBO holen
        with FlexDayMapper() as mapper:
            return mapper.find_all()
    
    def get_flex_day_by_id(self, id):
        # FlexDayBO mit gegebener Id holen
        with FlexDayMapper() as mapper:
            return mapper.find_by_key(id)

    def create_flex_day(self, start, end, startevent, endevent):
        # FlexDayBO erstellen
        work_obj = FlexDayBO()
        work_obj.set_start(start)
        work_obj.set_end(end)
        work_obj.set_start_event(startevent)
        work_obj.set_end_event(endevent)

        with FlexDayMapper() as mapper:
            return mapper.insert(work_obj)

    def save_flex_day(self, flex_day_obj):
        # Änderungen in FlexDayBO speichern
        with FlexDayMapper() as mapper:
            mapper.update(flex_day_obj)
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "flexDayId", flex_day_obj.get_id(), flex_day_obj.get_type())
                print(timeinterval)
                mapper.update(timeinterval)
                self.save_time_interval_booking(timeinterval)

    def delete_flex_day(self, flexday_obj):
        # @author Mihriban Dogan (https://github.com/mihriban-dogan)
        # FlexDayBO löschen
        with FlexDayStartMapper() as mapper:
            flexday_begin = mapper.find_by_key(
                flexday_obj.get_start_event())
        with FlexDayEndMapper() as mapper:
            flexday_end = mapper.find_by_key(
                flexday_obj.get_end_event())
        with EventMapper() as mapper:
            startevent = mapper.find_by_foreign_key_and_type(
                "flex_day_start_id", flexday_begin.get_id(), flexday_begin.get_type())
        with EventMapper() as mapper:
            endevent = mapper.find_by_foreign_key_and_type(
                "flex_day_end_id", flexday_end.get_id(), flexday_end.get_type())
        with EventBookingMapper() as mapper:
            starteventbooking = mapper.find_by_event_id(startevent.get_id())
        with EventBookingMapper() as mapper:
            endeventbooking = mapper.find_by_event_id(endevent.get_id())
        with TimeIntervalMapper() as mapper:
            timeinterval = mapper.find_by_foreign_key_and_type(
                "flexDayId", flexday_obj.get_id(), flexday_obj.get_type())
        with TimeIntervalBookingMapper() as mapper:
            timeintervalbooking = mapper.find_by_timeinterval_id(
                timeinterval.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")

        with BookingMapper() as mapper:
            mapper.delete(booking)
        with TimeIntervalBookingMapper() as mapper:
            mapper.delete(timeintervalbooking)
        with TimeIntervalMapper() as mapper:
            mapper.delete(timeinterval)
        with FlexDayMapper() as mapper:
            mapper.delete(flexday_obj)
        with EventBookingMapper() as mapper:
            mapper.delete(starteventbooking)
        with EventBookingMapper() as mapper:
            mapper.delete(endeventbooking)
        with EventMapper() as mapper:
            mapper.delete(startevent)
        with EventMapper() as mapper:
            mapper.delete(endevent)
        with FlexDayStartMapper() as mapper:
            mapper.delete(flexday_begin)
        with FlexDayEndMapper() as mapper:
            mapper.delete(flexday_end)

    def get_flex_days_by_date(self, date):
        # FlexDayBO mit gegebenen Date holen
        with FlexDayMapper() as mapper:
            return mapper.find_by_date(date)

    def get_flex_days_by_time_period(self, startdate, enddate):    
        # FlexDayBO aus gegebenen Zeitraum holen
        with FlexDayMapper() as mapper:
            return mapper.find_by_time_period(startdate, enddate)

    """
    ProjectDuration Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """

    def get_all_project_durations(self):    
        # alle ProjectDurationBO holen
        with ProjectDurationMapper() as mapper:
            return mapper.find_all()


    def get_project_duration_by_id(self, id):    
        # ProjectDurationBO mit gegebener Id holen
        with ProjectDurationMapper() as mapper:
            return mapper.find_by_key(id)


    def create_project_duration(self, start, end, startevent, endevent, project_id):    
        # ProjectDurationBO erstellen
        project_duration_obj = ProjectDurationBO()
        project_duration_obj.set_start(start)
        project_duration_obj.set_end(end)
        project_duration_obj.set_start_event(startevent)
        project_duration_obj.set_end_event(endevent)
        project_duration_obj.set_type("ProjectDuration")
        project_duration_obj.set_project_id(project_id)

        with ProjectDurationMapper() as mapper:
            return mapper.insert(project_duration_obj)

    
    def save_project_duration(self, project_duration_obj):
        # Änderungen in ProjectDurationBO speichern
        with ProjectDurationMapper() as mapper:
            mapper.update(project_duration_obj)

    def delete_project_duration(self, project_duration_obj):
        # @author Mihriban Dogan (https://github.com/mihriban-dogan)
        # ProjectDurationBO löschen
        with TimeIntervalMapper() as mapper:
            timeinterval = mapper.find_by_foreign_key_and_type(
                "projectDurationId", project_duration_obj.get_id(), project_duration_obj.get_type())
        with TimeIntervalBookingMapper() as mapper:
            timeintervalbooking = mapper.find_by_timeinterval_id(
                timeinterval.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")

        with BookingMapper() as mapper:
            mapper.delete(booking)
        with TimeIntervalBookingMapper() as mapper:
            mapper.delete(timeintervalbooking)
        with TimeIntervalMapper() as mapper:
            mapper.delete(timeinterval)
        with ProjectDurationMapper() as mapper:
            mapper.delete(project_duration_obj)
    
    def get_project_durations_by_date(self, date):
        # ProjectDurationBO mit gegebenen Date holen
        with ProjectDurationMapper() as mapper:
            return mapper.find_by_date(date)

    def get_project_durations_by_time_period(self, startdate, enddate):
        # ProjectDurationBO innerhalb gegebener Zeitperiode holen
        with ProjectDurationMapper() as mapper:
            return mapper.find_by_time_period(startdate, enddate)

    def get_project_duration_by_project_id(self, id):
        # ProjektDurationBO mit gegebener ProjectId holen
        with ProjectDurationMapper() as mapper:
            return mapper.find_by_project_id(id)

    def get_project_duration_interval(self, project_id):
        # @author Khadidja Kebaili (https://github.com/khadidja-kebaili)
        # Tage von Start bis Ende des Projects berechnen
        duration = self.get_project_duration_by_project_id(project_id)
        delta = duration.get_end() - duration.get_start()
        delta_float = round((delta.total_seconds() / 86400), 2)
        return delta_float

    """
    ProjectWork Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """

    def get_all_project_works(self):
        # alle ProjectWorkBO holen
        with ProjectWorkMapper() as mapper:
            return mapper.find_all()
    
    def get_project_work_by_id(self, id):
        # ProjectWorkBO mit gegebener Id holen
        with ProjectWorkMapper() as mapper:
            return mapper.find_by_key(id)

    def create_project_work(self, start, end, startevent, endevent, activity_id):
        # ProjectWorkBO erstellen
        project_work_obj = ProjectWorkBO()
        project_work_obj.set_start(start)
        project_work_obj.set_end(end)
        project_work_obj.set_start_event(startevent)
        project_work_obj.set_end_event(endevent)
        project_work_obj.set_type("ProjectWork")
        project_work_obj.set_activity_id(activity_id)

        with ProjectWorkMapper() as mapper:
            return mapper.insert(project_work_obj)

    def save_project_work(self, project_work_obj):
        # Änderungen in ProjectWorkBO speichern
        with ProjectWorkMapper() as mapper:
            mapper.update(project_work_obj)
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "projectWorkId", project_work_obj.get_id(), project_work_obj.get_type())
                print(timeinterval)
                mapper.update(timeinterval)
                self.save_time_interval_booking(timeinterval)

    def delete_project_work(self, project_work_obj):
        # @author Mihriban Dogan (https://github.com/mihriban-dogan)
        # ProjectWorkBO löschen
        with ProjectWorkBeginMapper() as mapper:
            project_work_begin = mapper.find_by_key(
                project_work_obj.get_start_event())
        with ProjectWorkEndMapper() as mapper:
            project_work_end = mapper.find_by_key(
                project_work_obj.get_end_event())
        with EventMapper() as mapper:
            startevent = mapper.find_by_foreign_key_and_type(
                "project_work_begin_id", project_work_begin.get_id(), project_work_begin.get_type())
        with EventMapper() as mapper:
            endevent = mapper.find_by_foreign_key_and_type(
                "project_work_end_id", project_work_end.get_id(), project_work_end.get_type())
        with EventBookingMapper() as mapper:
            starteventbooking = mapper.find_by_event_id(startevent.get_id())
        with EventBookingMapper() as mapper:
            endeventbooking = mapper.find_by_event_id(endevent.get_id())
        with TimeIntervalMapper() as mapper:
            timeinterval = mapper.find_by_foreign_key_and_type(
                "projectWorkId", project_work_obj.get_id(), project_work_obj.get_type())
        with TimeIntervalBookingMapper() as mapper:
            timeintervalbooking = mapper.find_by_timeinterval_id(
                timeinterval.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
        with BookingMapper() as mapper:
            mapper.delete(booking)
        with TimeIntervalBookingMapper() as mapper:
            mapper.delete(timeintervalbooking)
        with TimeIntervalMapper() as mapper:
            mapper.delete(timeinterval)
        with ProjectWorkMapper() as mapper:
            mapper.delete(project_work_obj)
        with EventBookingMapper() as mapper:
            mapper.delete(starteventbooking)
        with EventBookingMapper() as mapper:
            mapper.delete(endeventbooking)
        with EventMapper() as mapper:
            mapper.delete(startevent)
        with EventMapper() as mapper:
            mapper.delete(endevent)
        with ProjectWorkBeginMapper() as mapper:
            mapper.delete(project_work_begin)
        with ProjectWorkEndMapper() as mapper:
            mapper.delete(project_work_end)
        delta = project_work_obj.get_end() - project_work_obj.get_start()
        delta_float = round(((delta.total_seconds() / 60) / 60), 2)
        self.calculate_delta_for_project_work(
            booking, -delta_float, project_work_obj.get_activity_id())

    def get_project_works_by_date(self, date):
        # ProjectWorkBO mit gegebenen Date holen
        with ProjectWorkMapper() as mapper:
            return mapper.find_by_date(date)

    def get_project_works_by_time_period(self, startdate, enddate):        
        # ProjectWorkBO innerhalb gegebenen Zeitraum holen
        with ProjectWorkMapper() as mapper:
            return mapper.find_by_time_period(startdate, enddate)

    def get_project_works_by_activity_id(self, id):
        # ProjectWorkBO mit gegebener ActivityId holen
        with ProjectWorkMapper() as mapper:
            return mapper.find_all_by_activity_id(id)

    """
    Booking Methoden @author Mihriban Dogan (https://github.com/mihriban-dogan)
    """

    def get_timeinterval_booking_by_id(self, id):
        # Ein TimeIntervalBooking anhand der ID aus der Datenbank holen
        with TimeIntervalBookingMapper() as mapper:
            return mapper.find_by_key(id)

    def get_event_booking_by_id(self, id):
        # Ein EventBooking anhand der ID aus der Datenbank holen
        with EventBookingMapper() as mapper:
            return mapper.find_by_key(id)

    def get_booking_by_id(self, id):
        # Ein Booking anhand der ID aus der Datenbank holen
        with BookingMapper() as mapper:
            return mapper.find_by_key(id)

    def create_timeinterval_booking(self, timeintervalId):
        """Ein Timeinterval Booking anlegen"""

        timeintervalbooking = TimeIntervalBookingBO()
        timeintervalbooking.set_timeinterval_id(timeintervalId)

        with TimeIntervalBookingMapper() as mapper:
            return mapper.insert(timeintervalbooking)

    def create_event_booking(self, eventbookingId):
        """Ein Event Booking anlegen"""

        eventbooking = EventBookingBO()
        eventbooking.set_event_id(eventbookingId)

        with EventBookingMapper() as mapper:
            return mapper.insert(eventbooking)

    def create_booking_for_timeinterval(self, userId, worktimeAccountId, type, eventbookingId):
        # Ein Booking für ein TimeIntervalBooking anlegen
        with TimeIntervalBookingMapper() as mapper:
            last_entry = mapper.find_last_entry()
            id = last_entry.get_id()
        booking = BookingBO()
        booking.set_user_id(userId)
        booking.set_work_time_account_id(worktimeAccountId)
        booking.set_type(type)
        booking.set_event_booking_id(eventbookingId)
        booking.set_time_interval_booking_id(id)

        with BookingMapper() as mapper:
            return mapper.insert(booking)

    def create_booking_for_event(self, userId, worktimeAccountId, type, timeintervalbookingId):
        # Ein Booking für ein EventBooking anlegen
        with EventBookingMapper() as mapper:
            last_entry = mapper.find_last_entry()
            id = last_entry.get_id()

        booking = BookingBO()
        booking.set_user_id(userId)
        booking.set_work_time_account_id(worktimeAccountId)
        booking.set_type(type)
        booking.set_event_booking_id(id)
        booking.set_time_interval_booking_id(timeintervalbookingId)

        with BookingMapper() as mapper:
            return mapper.insert(booking)

    def get_all_timeinterval_bookings_for_user(self, user):
        """
        alle TimeIntervalSubklassen für den User werden geholt.
        Über den User werden die entsprechenden Bookings, dann TimeIntervalBookings,
        Timeintervals und dann die Subklassen geholt.
        Zusätzlich werden die verknüften Events geholt 
        """
        booking_types = ["timeintervals", "events"]
        res_ti = []
        res_ti_e = []
        res_final = []

        # alle Intervalbookings holen
        with BookingMapper() as mapper:
            timeintervalbookings = mapper.find_timeinterval_bookings_by_user_id(
                user.get_id())

        # Zeitintervalle holen
        for elem in timeintervalbookings:
            timeintervalbookingid = elem.get_time_interval_booking_id()
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_key(timeintervalbookingid)
                id = timeintervalbooking.get_timeinterval_id()
            # entsprechend des Types in Zeitinterval werden die verschiedenen Punkte für
            # die Event genutzt
            with TimeIntervalMapper() as mapper:
                timeintervals = mapper.find_by_key(id)
                type = timeintervals.get_type()
                if type == 'break':
                    res = self.get_break_by_id(timeintervals.get_break_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with BreakBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with BreakEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with BreakBeginMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with BreakEndMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                if type == 'illness':
                    res = self.get_illness_by_id(
                        timeintervals.get_illness_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with IllnessBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with IllnessEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with IllnessBeginMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with IllnessEndMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                if type == 'ProjectDuration':
                    res = self.get_project_duration_by_id(
                        timeintervals.get_project_duration_id())
                    res_ti.append(res)
                if type == 'ProjectWork':
                    res = self.get_project_work_by_id(
                        timeintervals.get_project_work_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with ProjectWorkBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with ProjectWorkEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with ProjectWorkBeginMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with ProjectWorkEndMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                if type == 'vacation':
                    res = self.get_vacation_by_id(
                        timeintervals.get_vacation_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with VacationBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with VacationEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with VacationBeginMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with VacationEndMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                if type == 'work':
                    res = self.get_work_by_id(timeintervals.get_work_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with ComingMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with GoingMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with ComingMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with GoingMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                if type == 'flexday':
                    res = self.get_flex_day_by_id(
                        timeintervals.get_flex_day_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with FlexDayStartMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with FlexDayEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with FlexDayStartMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with FlexDayEndMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
        res_final = [res_ti, res_ti_e]
        res_final_dict = dict(zip(booking_types, res_final))
        print(res_final_dict)
        return res_final_dict

    def get_all_timeintervals_without_events_for_user(self, user):
        """
        Gibt alle Zeitintervalle-Subklassen zurück ohne die verknüpften
        Events
        """
        booking_types = ["timeintervals", "events"]
        res_ti = []
        res_ti_e = []
        res_final = []

        # Timeintervalbookings geholt
        with BookingMapper() as mapper:
            timeintervalbookings = mapper.find_timeinterval_bookings_by_user_id(
                user.get_id())

        # Timeinterval holen
        for elem in timeintervalbookings:
            timeintervalbookingid = elem.get_time_interval_booking_id()
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_key(timeintervalbookingid)
                id = timeintervalbooking.get_timeinterval_id()
            # Mapper entsprechend des Types wählen
            with TimeIntervalMapper() as mapper:
                timeintervals = mapper.find_by_key(id)
                type = timeintervals.get_type()
                if type == 'break':
                    res = self.get_break_by_id(timeintervals.get_break_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with BreakBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with BreakEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with BreakBeginMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with BreakEndMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                if type == 'illness':
                    res = self.get_illness_by_id(
                        timeintervals.get_illness_id())
                    res_ti.append(res)
                if type == 'ProjectDuration':
                    res = self.get_project_duration_by_id(
                        timeintervals.get_project_duration_id())
                    res_ti.append(res)
                if type == 'ProjectWork':
                    res = self.get_project_work_by_id(
                        timeintervals.get_project_work_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with ProjectWorkBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with ProjectWorkEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with ProjectWorkBeginMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with ProjectWorkEndMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                if type == 'vacation':
                    res = self.get_vacation_by_id(
                        timeintervals.get_vacation_id())
                    res_ti.append(res)
                if type == 'work':
                    res = self.get_work_by_id(timeintervals.get_work_id())
                    res_ti.append(res)
                if type == 'flexday':
                    res = self.get_flex_day_by_id(
                        timeintervals.get_flex_day_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with FlexDayStartMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with FlexDayEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with FlexDayStartMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with FlexDayEndMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
        res_final = [res_ti, res_ti_e]
        res_final_dict = dict(zip(booking_types, res_final))
        print(res_final_dict)
        return res_final_dict

    def get_project_duration_bookings_for_user(self, user):
        """
        Die ProjectdurationBOs für einen User holen
        """
        res_ti = []

        # alle TimeIntervalBookings des Users holen
        with BookingMapper() as mapper:
            timeintervalbookings = mapper.find_timeinterval_bookings_by_user_id(
                user.get_id())

        # alle TimeIntervalBookings durchgehen um an ProjectDuration zu kommen
        for elem in timeintervalbookings:
            timeintervalbookingid = elem.get_time_interval_booking_id()
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_key(timeintervalbookingid)
                id = timeintervalbooking.get_timeinterval_id()
            with TimeIntervalMapper() as mapper:
                timeintervals = mapper.find_by_key(id)
                type = timeintervals.get_type()
                if type == 'ProjectDuration':
                    res = self.get_project_duration_by_id(
                        timeintervals.get_project_duration_id())
                    res_ti.append(res)

        return res_ti

    def get_work_bookings_for_user(self, user):
        """
        Die WorkBOs für einen User holen
        """
        res_ti = []

        with BookingMapper() as mapper:
            timeintervalbookings = mapper.find_timeinterval_bookings_by_user_id(
                user.get_id())

        for elem in timeintervalbookings:
            timeintervalbookingid = elem.get_time_interval_booking_id()
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_key(timeintervalbookingid)
                id = timeintervalbooking.get_timeinterval_id()
            with TimeIntervalMapper() as mapper:
                timeintervals = mapper.find_by_key(id)
                type = timeintervals.get_type()
                if type == 'work':
                    res = self.get_work_by_id(
                        timeintervals.get_work_id())
                    res_ti.append(res)

        return res_ti

    def get_vacation_bookings_for_user(self, user):
        """
        Die VacationBOs für einen User holen
        """
        res_ti = []

        with BookingMapper() as mapper:
            timeintervalbookings = mapper.find_timeinterval_bookings_by_user_id(
                user.get_id())

        for elem in timeintervalbookings:
            timeintervalbookingid = elem.get_time_interval_booking_id()
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_key(timeintervalbookingid)
                id = timeintervalbooking.get_timeinterval_id()
            with TimeIntervalMapper() as mapper:
                timeintervals = mapper.find_by_key(id)
                type = timeintervals.get_type()
                if type == 'vacation':
                    res = self.get_vacation_by_id(
                        timeintervals.get_vacation_id())
                    res_ti.append(res)

        return res_ti

    def get_illness_bookings_for_user(self, user):
        """
        DIe IllnessBOs für einen User holen
        """
        res_ti = []

        with BookingMapper() as mapper:
            timeintervalbookings = mapper.find_timeinterval_bookings_by_user_id(
                user.get_id())

        for elem in timeintervalbookings:
            timeintervalbookingid = elem.get_time_interval_booking_id()
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_key(timeintervalbookingid)
                id = timeintervalbooking.get_timeinterval_id()
            with TimeIntervalMapper() as mapper:
                timeintervals = mapper.find_by_key(id)
                type = timeintervals.get_type()
                if type == 'illness':
                    res = self.get_illness_by_id(
                        timeintervals.get_illness_id())
                    res_ti.append(res)

        return res_ti

    def get_project_work_bookings_for_user(self, user):
        """
        Die ProjectWorkBOs für User holen
        """
        res_ti = []

        with BookingMapper() as mapper:
            timeintervalbookings = mapper.find_timeinterval_bookings_by_user_id(
                user.get_id())

        for elem in timeintervalbookings:
            timeintervalbookingid = elem.get_time_interval_booking_id()
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_key(timeintervalbookingid)
                id = timeintervalbooking.get_timeinterval_id()
            with TimeIntervalMapper() as mapper:
                timeintervals = mapper.find_by_key(id)
                type = timeintervals.get_type()
                if type == 'ProjectWork':
                    res = self.get_project_work_by_id(
                        timeintervals.get_project_work_id())
                    res_ti.append(res)

        return res_ti

    # Alle EventBookings für einen User holen
    def get_all_event_bookings_for_user(self, user):
        '''Als erstes werden die alle ids geholt, danach der Fremdschlüssel EventbookingId 
        und dieser wird dann in der Tabelle Eventbooking eingefügt 
        und dort wird dann nach dem FK Eventid gesucht'''

        res_e = []

        with BookingMapper() as mapper:
            eventbookings = mapper.find_event_bookings_by_user_id(
                user.get_id())

        for elem in eventbookings:
            eventbookingid = elem.get_event_booking_id()
            with EventBookingMapper() as mapper:
                eventbooking = mapper.find_by_key(eventbookingid)
                id = eventbooking.get_event_id()
            with EventMapper() as mapper:
                events = mapper.find_by_key(id)
                type = events.get_type()
            if type == 'breakBegin':
                res = self.get_break_begin_by_id(events.get_break_begin_id())
                res_e.append(res)
            if type == 'breakEnd':
                res = self.get_break_end_by_id(events.get_break_end_id())
                res_e.append(res)
            if type == 'illnessBegin':
                res = self.get_illness_begin_by_id(
                    events.get_illness_begin_id())
                res_e.append(res)
            if type == 'illnessEnd':
                res = self.get_illness_end_by_id(events.get_illness_end_id())
                res_e.append(res)
            if type == 'projectWorkBegin':
                res = self.get_project_work_begin_by_id(
                    events.get_project_work_begin_id())
                res_e.append(res)
            if type == 'projectWorkEnd':
                res = self.get_project_work_end_by_id(
                    events.get_project_work_end_id())
                res_e.append(res)
            if type == 'vacationBegin':
                res = self.get_vacation_begin_by_id(
                    events.get_vacation_begin_id())
                res_e.append(res)
            if type == 'vacationEnd':
                res = self.get_vacation_end_by_id(events.get_vacation_end_id())
                res_e.append(res)
            if type == 'coming':
                res = self.get_coming_by_id(events.get_coming_id())
                res_e.append(res)
            if type == 'going':
                res = self.get_going_by_id(events.get_going_id())
                res_e.append(res)
        print(res_e)
        return res_e

    # Alle Vacation/Illness Bookings für einen User holen
    def get_all_vacation_illness_work_event_bookings_for_user(self, user):
        '''Als erstes werden die alle ids geholt, danach der Fremdschlüssel EventbookingId 
        und dieser wird dann in der Tabelle Eventbooking eingefügt 
        und dort wird dann nach dem FK Eventid gesucht'''

        res_e = []

        with BookingMapper() as mapper:
            eventbookings = mapper.find_event_bookings_by_user_id(
                user.get_id())

        for elem in eventbookings:
            eventbookingid = elem.get_event_booking_id()
            with EventBookingMapper() as mapper:
                eventbooking = mapper.find_by_key(eventbookingid)
                id = eventbooking.get_event_id()
            with EventMapper() as mapper:
                events = mapper.find_by_key(id)
                type = events.get_type()
            if type == 'illnessBegin':
                res = self.get_illness_begin_by_id(
                    events.get_illness_begin_id())
                res_e.append(res)
            if type == 'illnessEnd':
                res = self.get_illness_end_by_id(events.get_illness_end_id())
                res_e.append(res)
            if type == 'vacationBegin':
                res = self.get_vacation_begin_by_id(
                    events.get_vacation_begin_id())
                res_e.append(res)
            if type == 'vacationEnd':
                res = self.get_vacation_end_by_id(events.get_vacation_end_id())
                res_e.append(res)
            if type == 'coming':
                res = self.get_coming_by_id(events.get_coming_id())
                res_e.append(res)
            if type == 'going':
                res = self.get_going_by_id(events.get_going_id())
                res_e.append(res)
        print(res_e)
        return res_e
    
    def save_time_interval_booking(self, timeinterval):
        # TimeintervalBookings updaten
        with TimeIntervalBookingMapper() as mapper:
            timeintervalbooking = mapper.find_by_key(timeinterval.get_id())
            mapper.update(timeintervalbooking)
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "timeIntervalBookingId", timeintervalbooking.get_id(), "T")
            mapper.update(booking)

    
    def save_event_booking(self, event):
        # EventBookings updaten
        with EventBookingMapper() as mapper:
            eventbooking = mapper.find_by_key(event.get_id())
            mapper.update(eventbooking)
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "eventBookingId", eventbooking.get_id(), "E")
            if booking == None:
                pass
            else:
                mapper.update(booking)
            # if booking.get_type() == "E":
            #     mapper.update(booking)
            # else:
            #     pass

    

    def delete_time_interval_booking(self, timeinterval):
        # TimeintervalBookings löschen
        with TimeIntervalBookingMapper() as mapper:
            timeintervalbooking = mapper.find_by_key(timeinterval.get_id())
            mapper.delete(timeintervalbooking)
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "timeIntervalBookingId", timeintervalbooking.get_id(), "T")
            mapper.delete(booking)

    

    def delete_event_booking(self, event):
        # EventBookings löschen
        with EventBookingMapper() as mapper:
            eventbooking = mapper.find_by_key(event.get_id())
            mapper.delete(eventbooking)
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "eventBookingId", eventbooking.get_id(), "E")
            if booking.get_type() == "E":
                mapper.update(booking)
            else:
                pass

    """
    Arbeitszeiten für Buchungen berechnen @author Mihriban Dogan (https://github.com/mihriban-dogan)
    """

    
    def add_delta(self, tbooking):
        # Die Arbeitszeit für Break, Work und Flexday Buchungen berechnen
        timeintervalbookingid = tbooking.get_time_interval_booking_id()
        with TimeIntervalBookingMapper() as mapper:
            timeintervalbooking = mapper.find_by_key(timeintervalbookingid)
        with TimeIntervalMapper() as mapper:
            timeinterval = mapper.find_by_key(timeintervalbooking.get_id())
        if timeinterval.get_type() == "break":
            with BreakMapper() as mapper:
                breaks = mapper.find_by_key(
                    timeinterval.get_break_id())
                delta = breaks.get_end() - breaks.get_start()
                delta_float = round(((delta.total_seconds() / 60) / 60), 2)
                self.calculate_delta_break_flexdays(tbooking, delta_float)
        if timeinterval.get_type() == "work":
            with WorkMapper() as mapper:
                work = mapper.find_by_key(
                    timeinterval.get_work_id())
            if work.get_end() == None:
                with ComingMapper() as mapper:
                    start = mapper.get_coming_by_id(work.get_start_event())
                    end = mapper.get_going_by_if(work.get_end_event())
                delta = end - start
            else:
                delta = work.get_end() - work.get_start()
            delta_float = round(((delta.total_seconds() / 60) / 60), 2)
            print("Gearbeitete Zeit", delta_float)
            self.calculate_delta_work(tbooking, delta_float)
        if timeinterval.get_type() == "flexday":
            with FlexDayMapper() as mapper:
                flexdays = mapper.find_by_key(
                    timeinterval.get_flex_day_id())
            delta = flexdays.get_end() - flexdays.get_start()
            delta_float = round(((delta.total_seconds() / 60) / 60), 2)
            self.calculate_delta_break_flexdays(tbooking, delta_float)

    
    def add_delta_for_project_work(self, tbooking):
        # Die Arbeitszeit für ProjectWork Buchungen berechnen
        timeintervalbookingid = tbooking.get_time_interval_booking_id()
        with TimeIntervalBookingMapper() as mapper:
            timeintervalbooking = mapper.find_by_key(timeintervalbookingid)
        with TimeIntervalMapper() as mapper:
            timeinterval = mapper.find_by_key(timeintervalbooking.get_id())
        with ProjectWorkMapper() as mapper:
            projectwork = mapper.find_by_key(
                timeinterval.get_project_work_id())
        delta = projectwork.get_end() - projectwork.get_start()
        delta_float = round(((delta.total_seconds() / 60) / 60), 2)
        activityid = projectwork.get_activity_id()
        self.calculate_delta_for_project_work(
            tbooking, delta_float, activityid)

    
    def calculate_delta_for_project_work(self, tbooking, delta_float, activityid):
        # Die Arbeitszeit von der ProjectWork Buchung in die ProjectUser und Activity Tabelle einfügen
        print(delta_float)
        activity = self.get_activity_by_id(activityid)
        with ProjectUserMapper() as mapper:
            projectuser = mapper.find_project_user_by_user_id_and_project_id(
                tbooking.get_user_id(), activity.get_project_id())
            capacity = projectuser.get_capacity()
        if (projectuser.get_current_capacity() == None) or (projectuser.get_current_capacity() == 0):
            current_capacity = round((capacity - delta_float), 2)
            projectuser.set_current_capacity(current_capacity)
            with ProjectUserMapper() as mapper:
                mapper.update(projectuser)
        else:
            new_current_capacity = round(
                (projectuser.get_current_capacity() - delta_float), 2)
            projectuser.set_current_capacity(new_current_capacity)
            with ProjectUserMapper() as mapper:
                mapper.update(projectuser)

        if (activity.get_current_capacity() == None) or (activity.get_current_capacity() == 0):
            activity.set_current_capacity(delta_float)
            with ActivityMapper() as mapper:
                mapper.update(activity)
        else:
            new_current_capacity_a = round(
                (activity.get_current_capacity() + delta_float), 2)
            activity.set_current_capacity(new_current_capacity_a)
            with ActivityMapper() as mapper:
                mapper.update(activity)

    
    def calculate_delta_work(self, tbooking, delta_float):
        # Die Arbeitszeit für Work Buchungen in die WorkTimeAccount Tabelle einfügen
        with WorkTimeAccountMapper() as mapper:
            account = mapper.find_by_user_id(tbooking.get_user_id())
            print(account)
            contracttime = account.get_contract_time()
            print("Gearbeitete Zeit", delta_float)
        if delta_float < contracttime:
            deficit = delta_float - contracttime
            new_overtime = account.get_overtime() + deficit
            print("Neue Overtime", new_overtime)
            account.set_overtime(new_overtime)
            with WorkTimeAccountMapper() as mapper:
                return mapper.update(account)
        elif delta_float > contracttime:
            overtime = delta_float - contracttime
            new_overtime = account.get_overtime() + overtime
            print("Neue Overtime", new_overtime)
            account.set_overtime(new_overtime)
            with WorkTimeAccountMapper() as mapper:
                return mapper.update(account)
        elif delta_float == contracttime:
            pass

    
    def calculate_delta_break_flexdays(self, tbooking, delta_float):
        # Die Arbeitszeit für Flexdays in die WorkTimeAccount Tabelle einfügen
        with WorkTimeAccountMapper() as mapper:
            account = mapper.find_by_user_id(tbooking.get_user_id())

        new_overtime = round((account.get_overtime() - delta_float), 2)
        account.set_overtime(new_overtime)
        with WorkTimeAccountMapper() as mapper:
            return mapper.update(account)

    """
    User Methoden
    """

    def create_user(self, firstName, lastName, mailAdress, googleId):
        # Benutzer erstellen
        user_obj = UserBO()
        user_obj.set_first_name(firstName)
        user_obj.set_last_name(lastName)
        user_obj.set_mail_adress(mailAdress)
        user_obj.set_google_user_id(googleId)

        with UserMapper() as mapper:
            return mapper.insert(user_obj)

    '''def get_user_by_first_name(self, first_name):
        with UserMapper() as mapper:
            return mapper.find_by_first_name(first_name)'''

    def get_user_by_last_name(self, last_name):
        # User mit gegebenen Nachnamen holen
        with UserMapper() as mapper:
            return mapper.find_by_last_name(last_name)

    def get_user_by_mail_adress(self, mail_adress):
        # User via Email Adresse finden
        with UserMapper() as mapper:
            return mapper.find_by_mail(mail_adress)

    def get_user_by_google_user_id(self, string):
        # User via GoogleId finden
        with UserMapper() as mapper:
            return mapper.find_by_googleuserid(string)

    # def get_user_by_user_name(self, user_name):
    #     with UserMapper() as mapper:
    #         return mapper.find_by_user_name(user_name)

    def get_user_by_id(self, number):
        # User nach Id holen
        with UserMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_users(self):
        # alle User holen
        with UserMapper() as mapper:
            return mapper.find_all()

    def save_user(self, user_obj):
        # Änderungen am UserBO abspeichern
        with UserMapper() as mapper:
            mapper.update(user_obj)

    def delete_user(self, user_obj):
        # User löschen und alle damit verbundenen Komponenten
        projectuserlist = self.get_project_user_by_user_id(user_obj.get_id())
        bookings = self.get_all_timeinterval_bookings_for_user(user_obj)
        eventbookinglist = self.get_all_vacation_illness_work_event_bookings_for_user(
            user_obj)
        print("Eventbookinglist", eventbookinglist)
        if bookings is not None:
            for key, values in bookings.items():
                if key == "timeintervals":
                    for elem in values:
                        if elem.get_type() == "Work":
                            self.delete_work(elem)
                        if elem.get_type() == "Break":
                            self.delete_break(elem)
                        if elem.get_type() == "Flexday":
                            self.delete_flex_day(elem)
                        if elem.get_type() == "Illness":
                            self.delete_illness(elem)
                        if elem.get_type() == "ProjectDuration":
                            self.delete_project_duration(elem)
                        if elem.get_type() == "ProjectWork":
                            self.delete_project_work(elem)
                        if elem.get_type() == "Vacation":
                            self.delete_vacation(elem)
                # if key == "events":
                #     for elem in values:
                #         if elem.get_type() == "breakbegin":
                #             self.delete_break_begin(elem)
                #         if elem.get_type() == "breakend":
                #             self.delete_breakEnd(elem)
                #         if elem.get_type() == "coming":
                #             self.delete_coming(elem)
                #         if elem.get_type() == "going":
                #             self.delete_going(elem)
                #         if elem.get_type() == "flexdaystart":
                #             self.delete_flex_day_start(elem)
                #         if elem.get_type() == "flexdayend":
                #             self.delete_flex_day_end(elem)
                #         if elem.get_type() == "projectworkbegin":
                #             self.delete_project_work_begin(elem)
                #         if elem.get_type() == "projectworkend":
                #             self.delete_project_work_end(elem)

            if not projectuserlist:
                pass
            else:
                for projectuser in projectuserlist:
                    with ProjectUserMapper() as mapper:
                        mapper.delete(projectuser)
            if not eventbookinglist:
                with UserMapper() as mapper:
                    mapper.delete(user_obj)
            else:
                for eventbooking in eventbookinglist:
                    if eventbooking.get_type() == "illnessbegin":
                        self.delete_illness_begin(eventbooking)
                    if eventbooking.get_type() == "illnessend":
                        self.delete_illness_end(eventbooking)
                    if eventbooking.get_type() == "vacationbegin":
                        self.delete_vacation_begin(eventbooking)
                    if eventbooking.get_type() == "vacationend":
                        self.delete_vacation_end(eventbooking)
                    if eventbooking.get_type() == "coming":
                        self.delete_coming(eventbooking)
                    if eventbooking.get_type() == "going":
                        self.delete_going(eventbooking)
                    with UserMapper() as mapper:
                        mapper.delete(user_obj)
                with UserMapper() as mapper:
                    mapper.delete(user_obj)

    """
    WorkTimeAccount Methoden
    """

    def create_worktimeaccount(self, userId, contractTime, overTime):
        #Worktimeaccount erstellen
        worktimeaccount_obj = WorkTimeAccountBO()
        worktimeaccount_obj.set_user_id(userId)
        worktimeaccount_obj.set_contract_time(contractTime)
        worktimeaccount_obj.set_overtime(overTime)

        with WorkTimeAccountMapper() as mapper:
            return mapper.insert(worktimeaccount_obj)

    def get_worktimeaccount_by_user_id(self, user_id):
        #Worktimeaccount nach UserId finden
        with WorkTimeAccountMapper() as mapper:
            return mapper.find_by_user_id(user_id)

    def get_worktimeaccount_by_id(self, id):
        #Worktimeaccount nach Id finden
        with WorkTimeAccountMapper() as mapper:
            return mapper.find_by_key(id)

    def get_all_worktimeaccounts(self):
        #alle Worktimeaccounts finden
        with WorkTimeAccountMapper() as mapper:
            return mapper.find_all()

    def save_worktimeaccount(self, worktimeaccount_obj):
        # Änderungen im WorkTimeAccount abspeichern
        with WorkTimeAccountMapper() as mapper:
            mapper.update(worktimeaccount_obj)

    def delete_worktimeaccount(self, worktimeaccount_obj):
        # Worktimeaccount löschen
        with WorkTimeAccountMapper() as mapper:
            mapper.delete(worktimeaccount_obj)

    """
    @author [Vi Nam Le] (https://github.com/vinamle)
    Project
    """
    
    def create_project(self, name, commissioner, user_id):
        # Projekt erstellen
        project = ProjectBO()
        project.set_name(name)
        project.set_commissioner(commissioner)
        project.set_user_id(user_id)
        with ProjectMapper() as mapper:
            return mapper.insert(project)

    def get_project_by_id(self, id):
        # Projekt via Id holen
        with ProjectMapper() as mapper:
            return mapper.find_by_key(id)

    def get_last_project_entry(self):
        # letzten Eintrag von Projekt holen
        with ProjectMapper() as mapper:
            return mapper.find_last_entry()

    def get_all_projects(self):
        # alle Projekte holen
        with ProjectMapper() as mapper:
            return mapper.find_all()

    def save_project(self, project):
        # Änderungen im Projekt speichern
        with ProjectMapper() as mapper:
            mapper.update(project)

    def delete_project(self, project):
        # Projekt löschen
        members = self.get_all_project_members(project.get_id())
        activities = self.get_activities_by_project_id(project.get_id())
        # projectdurations = []
        # projectworks = []
        for elem in members:
            user = self.get_user_by_id(elem.get_user_id())
            projectduration = self.get_project_duration_bookings_for_user(
                user)
            for projectdurationentry in projectduration:
                # projectdurations.append(entry)
                self.delete_project_duration(projectdurationentry)

            projectwork = self.get_project_work_bookings_for_user(
                user)
            for projectworkentry in projectwork:
                # projectworks.append(secondentry)
                self.delete_project_work(projectworkentry)
            with ProjectUserMapper() as mapper:
                mapper.delete(elem)
        for elem in activities:
            self.delete_activity(elem)

        with ProjectMapper() as mapper:
            mapper.delete(project)
    
    def get_projects_by_user_id(self, id):
        # Projekt via UserId holen
        with ProjectMapper() as mapper:
            return mapper.find_projects_by_user_id(id)
    
    def get_by_project_name(self, name):
        # Projekt via Name holen
        with ProjectMapper() as mapper:
            mapper.find_by_project_name(name)

    """
    @author [Vi Nam Le] (https://github.com/vinamle)
    Projectuser
    """

    def create_projectuser(self, project_id, user_id, capacity, current):
        # ProjectUser erstellen
        projectuser = ProjectUserBO()
        projectuser.set_project_id(project_id)
        projectuser.set_user_id(user_id)
        projectuser.set_capacity(capacity)
        projectuser.set_current_capacity(current)
        with ProjectUserMapper() as mapper:
            return mapper.insert(projectuser)

    
    def get_projectuser_by_id(self, id):
        # ProjectUser via Id holen
        with ProjectUserMapper() as mapper:
            return mapper.find_by_key(id)
    
    def get_project_user_by_user_id(self, id):
        # ProjectUser via UserId holen
        with ProjectUserMapper() as mapper:
            return mapper.find_project_user_by_user_id(id)

    def get_all_projectusers(self):
        # alle ProjectUser holen
        with ProjectUserMapper() as mapper:
            return mapper.find_all()

    def save_projectuser(self, projectuser):
        # Änderungen von ProjectUser speichern
        with ProjectUserMapper() as mapper:
            mapper.update(projectuser)

    def delete_projectuser(self, projectuser):
        # ProjectUser löschen
        with ProjectUserMapper() as mapper:
            mapper.delete(projectuser)
    
    def get_all_project_members(self, project_id):
        # ProjectUser via ProjectId holen
        liste = self.get_all_projectusers()
        result = []
        for elem in liste:
            if elem.get_project_id() == project_id:
                result.append(elem)
        return result

    def get_projectuser_by_project_and_user(self, projectid, userid):
        with ProjectUserMapper() as mapper:
            return mapper.find_by_projectid_userid(projectid, userid)

    """
    @author [Vi Nam Le] (https://github.com/vinamle)
    Activity
    """
    
    def create_activity(self, name, capacity, project_id, current_capacity):
        # Activity erstellen
        activity = ActivityBO()
        activity.set_name(name)
        activity.set_capacity(capacity)
        activity.set_project_id(project_id)
        activity.set_current_capacity(current_capacity)

        with ActivityMapper() as mapper:
            return mapper.insert(activity)

    def get_activity_by_id(self, id):
        # Acticity via Id holen
        with ActivityMapper() as mapper:
            return mapper.find_by_key(id)

    def get_all_activities(self):
        # alle Activities holen
        with ActivityMapper() as mapper:
            return mapper.find_all()

    def save_activity(self, activity):
        # Änderungen in Activity speichern
        with ActivityMapper() as mapper:
            mapper.update(activity)

    def delete_activity(self, activity):
        # Activity löschen
        x = self.get_project_works_by_activity_id(activity.get_id())
        for elem in x:
            self.delete_project_work(elem)
        with ActivityMapper() as mapper:
            mapper.delete(activity)

    def get_by_name(self, name):
        # Acticity via Namen holen
        with ActivityMapper() as mapper:
            return mapper.find_by_name(name)

    def get_activities_by_project_id(self, project_id):
        # Activity via ProjectId holen
        with ActivityMapper() as mapper:
            return mapper.find_all_by_project_id(project_id)

    """
    Zuordnung Project-User, geleistete Projektarbeit und zugehörige Projekte bzw. Aktivitäten
    @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)
     """

    def get_all_timeinterval_bookings(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)
        Methode holt alle Timeinterval-Buchungen aus der Datenbank
        :return: Array mit Timeintervalbookings.
        """
        with TimeIntervalBookingMapper() as mapper:
            return mapper.find_all()

    def get_all_bookings_for_timeinterval(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)
        Methode holt alle Buchungen aus der Datenbank, die ein Timeinterval enthalten
        :return: Array mit BookingBOs
        """
        with BookingMapper() as mapper:
            return mapper.find_by_type('T')

    def get_all_bookings_for_events(self):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)
        Methode holt alle Buchungen aus der Datenbank, die ein Timeinterval enthalten
        :return: Array mit BookingBOs
        """
        with BookingMapper() as mapper:
            return mapper.find_by_type('E')

    def get_project_by_name(self, name):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Lädt Projekte aus der Datenbank und gibt dasjenige Projekt mit dem gesuchten Namen zurück.
        :param name: Name des zu holenden Projekts
        :return: ProjectBO
        """
        projects = self.get_all_projects()
        for elem in projects:
            if elem.get_name() == name:
                return elem

    def get_projects_for_admin(self, admin):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Lädt Projekte aus der Datenbank und gibt dasjenige Projekt mit dem gesuchten Admin zurück.
        :param admin: eingetragene UserId des Admins
        :return: Admin (UserBO)
        """
        all_projects = self.get_all_projects()
        projects_for_admin = []
        for elem in all_projects:
            if elem.get_user_id() == admin:
                projects_for_admin.append(elem)
        return projects_for_admin

    def get_projects_for_user(self, id):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Lädt Projekte aus der Datenbank und gibt diejenigen Projekte zurück, die als UserID die gesuchte id haben.
        :param id: 
        :return: 
        """
        user = self.get_user_by_id(id)
        all_projects = self.get_all_projects()
        all_project_user = self.get_all_projectusers()
        projects = []
        projects_of_user = []
        for elem in all_project_user:
            if elem.get_user_id() == user.get_id():
                projects.append(elem)
        for elem in all_projects:
            for x in projects:
                if elem.get_id() == x.get_project_id():
                    projects_of_user.append(elem)
        return projects_of_user

    def get_activities_by_project_id_and_user_id(self, project_id, user_id):
        """
        Alle Aktivitäten aus der Datenbank laden, für ein Projekt dem der User zugeordnet ist.
        :param project_id: Projekt-Id
        :param user_id: User-Id des Projekt-Users bzw. members
        :return: Array mit ActivityBOs
        """
        projects_for_user = self.get_projects_for_user(user_id)
        activities = []
        for elem in projects_for_user:
            if elem.get_id() == project_id:
                activities.append(
                    self.get_activities_by_project_id(elem.get_id()))
        return activities

    def get_actual_working_time_for_user_by_activity_id(self, user_id, activity_id):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Diese Methode lädt die TimeintervalBOs, Timeinterval-BookingBOs, BookingBOs und Aktivitäten aus der
        Datenbank und verknüpft sie so miteinander, dass man als Wert die tatsächlich gebuchte Arbeitszeit (in h)
        eines Projektmitarbeiters für eine bestimmte Aktivität zurückerhält.
        :param user_id: Projektuser-Id
        :param activity_id: Aktivitäts-Id
        :return: Zeit in Stunden (Float)
        """

        'Alle Timeintervals, Timerinterval-Buchungen und Buchungen'
        all_bookings = self.get_all_bookings_for_timeinterval()

        'Dies sind die Userspezifischen Bookings, Timeintervalle und deren Subklassen'
        bookings_of_user = []
        timeinterval_booking_of_user = []
        timeintervals_of_user = []
        projectwork_of_user = []
        project_work_for_this_activity_of_user = []

        'Hier sind alle Zeiten des Users für eine Aktivität'
        sum_time = []

        '''In diesem Schritt werden von den BookingBOs diejenigen selektiert, die dem User zugeordnet werden.'''
        for elem in all_bookings:
            #print('bookings:', elem.get_user_id())
            if elem.get_user_id() == user_id:
                bookings_of_user.append(elem)
        '''Check ob es Einträge gibt, ansonsten return 0 '''
        if len(bookings_of_user) >= 1:
            '''Von den Bookings werden diejenigen selektiert, die Timeintervalle beinhalten'''
            for elem in bookings_of_user:
                #print('in bookins_of_user: ', elem)
                ti_b_id = elem.get_time_interval_booking_id()
                ti_b = self.get_timeinterval_booking_by_id(ti_b_id)
                timeinterval_booking_of_user.append(ti_b)
            '''Von den Bookings des Users werden die Ids für die Timeintervalle abgelesen und diese aus der Datenbank
               geleaden.'''
            for elem in timeinterval_booking_of_user:
                #print('in ti_b for user: ', elem)
                ti_id = elem.get_timeinterval_id()
                ti = self.get_timeinterval_by_id(ti_id)
                timeintervals_of_user.append(ti)
            '''Von den Zeitintervallen werden diejenigen selektiert, die als Typ projectwork besitzen'''
            for elem in timeintervals_of_user:
                #print('in ti for user: ', elem)
                if elem.get_type() == 'ProjectWork':
                    '''PrpjectWorkBOs, anhand der Timeinterval-Bookings des Users, werden aus der Datenbank geladen'''
                    project_work = self.get_project_work_by_id(
                        elem.get_project_work_id())
                    projectwork_of_user.append(project_work)
            '''Von den PrjWrkBOs werden diejenigen selektiert, die zu der gesuchten Aktivität gebucht wurden.'''
            for elem in projectwork_of_user:
                #print('in projectwork for user: ', elem)
                if elem.get_activity_id() == activity_id:
                    '''Aktivitäten werden, anhand den ProjectWorkBOs des Users, aus der Datenbank geladen'''
                    project_work_for_this_activity_of_user.append(elem)
                    '''Berechnung des Zeitdeltas der tatsächlich geleisteten Projektarbeit'''
                    sum = elem.get_end() - elem.get_start()
                    sum = sum.total_seconds()
                    sum_time.append(sum)
            '''Umwandeln Sekunden in Stunden und aufrunden auf 2 Nachkommastellen.'''
            sum = math.fsum(sum_time) / 3600
            sum = round(sum, 2)
            return sum
        else:
            return 0

    def get_project_work_for_user_by_activity_id(self, user_id, activity_id):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Diese Methode lädt die TimeintervalBOs, Timeinterval-BookingBOs, BookingBOs und Aktivitäten aus der
        Datenbank und verknüpft sie so miteinander, dass man als Wert die tatsächlich gebuchte Arbeitszeit (in h)
        eines Projektmitarbeiters für eine bestimmte Aktivität zurückerhält.
        :param user_id: Projektuser-Id
        :param activity_id: Aktivitäts-Id
        :return: Zeit in Stunden (Float)
        """

        'Alle Timeintervals, Timerinterval-Buchungen und Buchungen'
        all_bookings = self.get_all_bookings_for_timeinterval()

        'Dies sind die Userspezifischen Bookings, Timeintervalle und deren Subklassen'
        bookings_of_user = []
        timeinterval_booking_of_user = []
        timeintervals_of_user = []
        projectwork_of_user = []
        project_work_for_this_activity_of_user = []

        'Hier sind alle Zeiten des Users für eine Aktivität'
        sum_time = []

        '''In diesem Schritt werden von den BookingBOs diejenigen selektiert, die dem User zugeordnet werden.'''
        for elem in all_bookings:
            # print('bookings:', elem.get_user_id())
            if elem.get_user_id() == user_id:
                bookings_of_user.append(elem)
        '''Check ob es Einträge gibt, ansonsten return 0 '''
        if len(bookings_of_user) >= 1:
            '''Von den Bookings werden diejenigen selektiert, die Timeintervalle beinhalten'''
            for elem in bookings_of_user:
                # print('in bookins_of_user: ', elem)
                ti_b_id = elem.get_time_interval_booking_id()
                ti_b = self.get_timeinterval_booking_by_id(ti_b_id)
                timeinterval_booking_of_user.append(ti_b)
            '''Von den Bookings des Users werden die Ids für die Timeintervalle abgelesen und diese aus der Datenbank
               geleaden.'''
            for elem in timeinterval_booking_of_user:
                # print('in ti_b for user: ', elem)
                ti_id = elem.get_timeinterval_id()
                ti = self.get_timeinterval_by_id(ti_id)
                timeintervals_of_user.append(ti)
            '''Von den Zeitintervallen werden diejenigen selektiert, die als Typ projectwork besitzen'''
            for elem in timeintervals_of_user:
                # print('in ti for user: ', elem)
                if elem.get_type() == 'ProjectWork':
                    '''PrpjectWorkBOs, anhand der Timeinterval-Bookings des Users, werden aus der Datenbank geladen'''
                    project_work = self.get_project_work_by_id(
                        elem.get_project_work_id())
                    projectwork_of_user.append(project_work)
            '''Von den PrjWrkBOs werden diejenigen selektiert, die zu der gesuchten Aktivität gebucht wurden.'''
            for elem in projectwork_of_user:
                # print('in projectwork for user: ', elem)
                if elem.get_activity_id() == activity_id:
                    '''Aktivitäten werden, anhand den ProjectWorkBOs des Users, aus der Datenbank geladen'''
                    project_work_for_this_activity_of_user.append(elem)

            return project_work_for_this_activity_of_user

    def get_project_work_for_user_within_timeframe(self,  user_id, activity_id, start, end):
        """
         @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

         Alle Eventsubklassen innerhalb einer gegebenen Zeitspanne
         :param user_id: UserId
         :param activity_id: Id der Aktivität deren Projektarbeit man laden möchte
         :param start: Start der Zeitspanne
         :param end: Ende der Zeitspanne
         :return: ProjectWork eines Users für eine Aktivität (Float)
        """

        all_bookings = self.get_all_bookings_for_timeinterval()

        'Dies sind die Userspezifischen Bookings, Timeintervalle und deren Subklassen'
        bookings_of_user = []
        timeinterval_booking_of_user = []
        timeintervals_of_user = []
        projectwork_of_user = []
        project_work_for_this_activity_of_user = []

        'Hier sind alle Zeiten des Users für eine Aktivität'
        sum_time = []

        '''In diesem Schritt werden von den BookingBOs diejenigen selektiert, die dem User zugeordnet werden.'''
        for elem in all_bookings:
            # print('bookings:', elem.get_user_id())
            if elem.get_user_id() == user_id:
                bookings_of_user.append(elem)
        '''Check ob es Einträge gibt, ansonsten return 0 '''
        if len(bookings_of_user) >= 1:
            '''Von den Bookings werden diejenigen selektiert, die Timeintervalle beinhalten'''
            for elem in bookings_of_user:
                # print('in bookins_of_user: ', elem)
                ti_b_id = elem.get_time_interval_booking_id()
                ti_b = self.get_timeinterval_booking_by_id(ti_b_id)
                timeinterval_booking_of_user.append(ti_b)
            '''Von den Bookings des Users werden die Ids für die Timeintervalle abgelesen und diese aus der Datenbank
               geleaden.'''
            for elem in timeinterval_booking_of_user:
                # print('in ti_b for user: ', elem)
                ti_id = elem.get_timeinterval_id()
                ti = self.get_timeinterval_by_id(ti_id)
                timeintervals_of_user.append(ti)
            '''Von den Zeitintervallen werden diejenigen selektiert, die als Typ projectwork besitzen'''
            for elem in timeintervals_of_user:
                # print('in ti for user: ', elem)
                if elem.get_type() == 'ProjectWork':
                    '''PrpjectWorkBOs, anhand der Timeinterval-Bookings des Users, werden aus der Datenbank geladen'''
                    project_work = self.get_project_work_by_id(
                        elem.get_project_work_id())
                    projectwork_of_user.append(project_work)
            '''Von den PrjWrkBOs werden diejenigen selektiert, die zu der gesuchten Aktivität gebucht wurden.'''
            for elem in projectwork_of_user:
                if self.in_between_times(elem.get_start(), start, end):
                    print(elem)
                # print('in projectwork for user: ', elem)
                    if elem.get_activity_id() == activity_id:
                        '''Aktivitäten werden, anhand den ProjectWorkBOs des Users, aus der Datenbank geladen'''
                        project_work_for_this_activity_of_user.append(elem)
                        '''Berechnung des Zeitdeltas der tatsächlich geleisteten Projektarbeit'''
                        sum = elem.get_end() - elem.get_start()
                        sum = sum.total_seconds()
                        sum_time.append(sum)
                '''Umwandeln Sekunden in Stunden und aufrunden auf 2 Nachkommastellen.'''
                sum = math.fsum(sum_time) / 3600
                sum = round(sum, 2)
                return sum
            else:
                return 0

    def get_timeintervals_for_user_within_timeframe(self, user_id, start, end):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Alle Timeinterval-Subklassen innerhalb einer gegebenen Zeitspanne
        :param user_id: UserId
        :param start: Start der Zeitspanne
        :param end: Ende der Zeitspanne
        :return: Array mit Timeinterval-subklassen
        """
        all_bookings = self.get_all_bookings_for_timeinterval()

        'Dies sind die userspezifischen Bookings, Timeintervalle und deren Subklassen'
        bookings_of_user = []
        timeinterval_booking_of_user = []
        timeintervals_of_user = []
        projectwork_of_user = []
        vacations = []
        all_illness = []
        breaks = []
        works = []
        projectdurations = []
        flexdays = []

        all_timeintervals = []
        within_timeframe = []
        '''In diesem Schritt werden von den BookingBOs diejenigen selektiert, die dem User zugeordnet werden.'''
        for elem in all_bookings:
            # print('bookings:', elem.get_user_id())
            if elem.get_user_id() == user_id:
                bookings_of_user.append(elem)
        '''Check ob es Einträge gibt, ansonsten return 0 '''
        if len(bookings_of_user) >= 1:
            '''Von den Bookings werden diejenigen selektiert, die Timeintervalle beinhalten'''
            for elem in bookings_of_user:
                # print('in bookins_of_user: ', elem)
                ti_b_id = elem.get_time_interval_booking_id()
                ti_b = self.get_timeinterval_booking_by_id(ti_b_id)
                timeinterval_booking_of_user.append(ti_b)
            '''Von den Bookings des Users werden die Ids für die Timeintervalle abgelesen und diese aus der Datenbank
               geleaden.'''
            for elem in timeinterval_booking_of_user:
                # print('in ti_b for user: ', elem)
                ti_id = elem.get_timeinterval_id()
                ti = self.get_timeinterval_by_id(ti_id)
                timeintervals_of_user.append(ti)
            '''Von den Zeitintervallen werden diejenigen selektiert, die als Typ projectwork besitzen'''
            for elem in timeintervals_of_user:
                if elem.get_type() == 'vacation':
                    vacation = self.get_vacation_by_id(
                        elem.get_vacation_id())
                    vacations.append(vacation)
                    all_timeintervals.append(vacation)
                if elem.get_type() == 'break':
                    break_bo = self.get_break_by_id(
                        elem.get_break_id())
                    breaks.append(break_bo)
                    all_timeintervals.append(break_bo)
                if elem.get_type() == 'ProjectWork':
                    project_work = self.get_project_work_by_id(
                        elem.get_project_work_id())
                    projectwork_of_user.append(project_work)
                    all_timeintervals.append(project_work)
                if elem.get_type() == 'ProjectDuration':
                    project_duration = self.get_project_duration_by_id(
                        elem.get_project_duration_id())
                    projectdurations.append(project_duration)
                    all_timeintervals.append(project_duration)
                if elem.get_type() == 'flexday':
                    flexday = self.get_flex_day_by_id(
                        elem.get_flex_day_id())
                    flexdays.append(flexday)
                    all_timeintervals.append(flexday)
                if elem.get_type() == 'illness':
                    illness = self.get_illness_by_id(elem.get_illness_id())
                    all_illness.append(illness)
                    all_timeintervals.append(illness)
                if elem.get_type() == 'work':
                    work = self.get_work_by_id(elem.get_work_id())
                    works.append(work)
                    all_timeintervals.append(work)
            '''Von den PrjWrkBOs werden diejenigen selektiert, die zu der gesuchten Aktivität gebucht wurden.'''
            for elem in all_timeintervals:
                if self.in_between_times(elem.get_start(), start, end) and self.in_between_times(elem.get_end(), start, end):
                    within_timeframe.append(elem)
        return within_timeframe

    def get_timeintervals_subclasses_for_user(self, user_id):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Alle Timeinterval-Subklassen innerhalb einer gegebenen Zeitspanne
        :param user_id: UserId
        :param start: Start der Zeitspanne
        :param end: Ende der Zeitspanne
        :return: Array mit Timeinterval-subklassen
        """
        all_bookings = self.get_all_bookings_for_timeinterval()

        'Dies sind die userspezifischen Bookings, Timeintervalle und deren Subklassen'
        bookings_of_user = []
        timeinterval_booking_of_user = []
        timeintervals_of_user = []
        projectwork_of_user = []
        vacations = []
        all_illness = []
        breaks = []
        works = []
        projectdurations = []
        flexdays = []

        all_timeintervals = []
        within_timeframe = []
        '''In diesem Schritt werden von den BookingBOs diejenigen selektiert, die dem User zugeordnet werden.'''
        for elem in all_bookings:
            # print('bookings:', elem.get_user_id())
            if elem.get_user_id() == user_id:
                bookings_of_user.append(elem)
        '''Check ob es Einträge gibt, ansonsten return 0 '''
        if len(bookings_of_user) >= 1:
            '''Von den Bookings werden diejenigen selektiert, die Timeintervalle beinhalten'''
            for elem in bookings_of_user:
                # print('in bookins_of_user: ', elem)
                ti_b_id = elem.get_time_interval_booking_id()
                ti_b = self.get_timeinterval_booking_by_id(ti_b_id)
                timeinterval_booking_of_user.append(ti_b)
            '''Von den Bookings des Users werden die Ids für die Timeintervalle abgelesen und diese aus der Datenbank
               geleaden.'''
            for elem in timeinterval_booking_of_user:
                # print('in ti_b for user: ', elem)
                ti_id = elem.get_timeinterval_id()
                ti = self.get_timeinterval_by_id(ti_id)
                timeintervals_of_user.append(ti)
            '''Von den Zeitintervallen werden diejenigen selektiert, die als Typ projectwork besitzen'''
            for elem in timeintervals_of_user:
                if elem.get_type() == 'vacation':
                    vacation = self.get_vacation_by_id(
                        elem.get_vacation_id())
                    vacations.append(vacation)
                    all_timeintervals.append(vacation)
                if elem.get_type() == 'break':
                    break_bo = self.get_break_by_id(
                        elem.get_break_id())
                    breaks.append(break_bo)
                    all_timeintervals.append(break_bo)
                if elem.get_type() == 'ProjectWork':
                    project_work = self.get_project_work_by_id(
                        elem.get_project_work_id())
                    projectwork_of_user.append(project_work)
                    all_timeintervals.append(project_work)
                if elem.get_type() == 'ProjectDuration':
                    pass
                    # project_duration = self.get_project_duration_by_id(
                    #     elem.get_project_duration_id())
                    # projectdurations.append(project_duration)
                    # all_timeintervals.append(project_duration)
                if elem.get_type() == 'flexday':
                    flexday = self.get_flex_day_by_id(
                        elem.get_flex_day_id())
                    flexdays.append(flexday)
                    all_timeintervals.append(flexday)
                if elem.get_type() == 'illness':
                    illness = self.get_illness_by_id(elem.get_illness_id())
                    all_illness.append(illness)
                    all_timeintervals.append(illness)
                if elem.get_type() == 'work':
                    work = self.get_work_by_id(elem.get_work_id())
                    works.append(work)
                    all_timeintervals.append(work)
            
        return all_timeintervals

    def get_events_for_user_within_timeframe(self, user_id, start, end):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Alle Eventsubklassen innerhalb einer gegebenen Zeitspanne
        :param user_id: UserId
        :param start: Start der Zeitspanne
        :param end: Ende der Zeitspanne
        :return: Array mit Eventsubklassen
        """
        all_bookings = self.get_all_bookings_for_events()
        # for elem in all_bookings:
        #     print(elem, 'Step 1')

        'Dies sind die Userspezifischen Bookings, Timeintervalle und deren Subklassen'
        bookings_of_user = []
        event_booking_of_user = []
        events_of_user = []

        all_events = []
        within_timeframe = []
        '''In diesem Schritt werden von den BookingBOs diejenigen selektiert, die dem User zugeordnet werden.'''
        for elem in all_bookings:
            # print('bookings:', elem.get_user_id())
            if elem.get_user_id() == user_id:
                bookings_of_user.append(elem)
                # print(elem, 'Step 2')
        '''Check ob es Einträge gibt, ansonsten return 0 '''
        if len(bookings_of_user) >= 1:
            '''Von den Bookings werden diejenigen selektiert, die Timeintervalle beinhalten'''
            for elem in bookings_of_user:
                # print('in bookins_of_user: ', elem)
                ev_b_id = elem.get_event_booking_id()
                ev_b = self.get_event_booking_by_id(ev_b_id)
                event_booking_of_user.append(ev_b)
                # for elem in timeinterval_booking_of_user:
                    # print(elem, 'Step 3')
            '''Von den Bookings des Users werden die Ids für die Timeintervalle abgelesen und diese aus der Datenbank
               geleaden.'''
            for elem in event_booking_of_user:
                # print('in ti_b for user: ', elem)
                ev_id = elem.get_event_id()
                ev = self.get_event_by_id(ev_id)
                events_of_user.append(ev)
            '''Von den Zeitintervallen werden diejenigen selektiert, die als Typ projectwork besitzen'''
            for elem in events_of_user:
                print(elem.get_type(), 'Step 4')
                if elem.get_type() == 'vacationEnd':
                    vacation = self.get_vacation_end_by_id(
                        elem.get_vacation_end_id())
                    all_events.append(vacation)
                if elem.get_type() == 'vacationBegin':
                    vacation = self.get_vacation_begin_by_id(
                        elem.get_vacation_begin_id())
                    all_events.append(vacation)
                if elem.get_type() == 'breakBegin':
                    break_bo = self.get_break_begin_by_id(
                        elem.get_break_begin_id())
                    all_events.append(break_bo)
                if elem.get_type() == 'breakEnd':
                    break_bo = self.get_break_end_by_id(
                        elem.get_break_end_id())
                    all_events.append(break_bo)
                if elem.get_type() == 'illnessBegin':
                    illnessbegin = self.get_illness_begin_by_id(
                        elem.get_illness_begin_id())
                    all_events.append(illnessbegin)
                if elem.get_type() == 'illnessEnd':
                    illnessend = self.get_illness_end_by_id(
                        elem.get_illness_end_id())
                    all_events.append(illnessend)
                if elem.get_type() == 'flexDayStart':
                    flexdaystart = self.get_flex_day_start_by_id(
                        elem.get_flex_day_start_id())
                    all_events.append(flexdaystart)
                if elem.get_type() == 'flexDayEnd':
                    flexdayend = self.get_flex_day_end_by_id(
                        elem.get_flex_day_end_id())
                    all_events.append(flexdayend)
                if elem.get_type() == 'projectWorkBegin':
                    project_work_begin = self.get_project_work_begin_by_id(
                        elem.get_project_work_begin_id())
                    all_events.append(project_work_begin)
                if elem.get_type() == 'projectWorkEnd':
                    project_work_end = self.get_project_work_end_by_id(
                        elem.get_project_work_end_id())
                    all_events.append(project_work_end)
                if elem.get_type() == 'coming':
                    coming = self.get_coming_by_id(
                        elem.get_coming_id())
                    all_events.append(coming)
                if elem.get_type() == 'going':
                    going = self.get_going_by_id(
                        elem.get_going_id())
                    all_events.append(going)
            '''Von den PrjWrkBOs werden diejenigen selektiert, die zu der gesuchten Aktivität gebucht wurden.'''
            for elem in all_events:
                if self.in_between_times(elem.get_time(), start, end):
                    within_timeframe.append(elem)
        return within_timeframe

    def get_events_subclasses_for_user(self, user_id):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Alle Eventsubklassen innerhalb einer gegebenen Zeitspanne
        :param user_id: UserId
        :param start: Start der Zeitspanne
        :param end: Ende der Zeitspanne
        :return: Array mit Eventsubklassen
        """
        all_bookings = self.get_all_bookings_for_events()
        # for elem in all_bookings:
        #     print(elem, 'Step 1')

        'Dies sind die Userspezifischen Bookings, Timeintervalle und deren Subklassen'
        bookings_of_user = []
        event_booking_of_user = []
        events_of_user = []

        all_events = []
        within_timeframe = []
        '''In diesem Schritt werden von den BookingBOs diejenigen selektiert, die dem User zugeordnet werden.'''
        for elem in all_bookings:
            # print('bookings:', elem.get_user_id())
            if elem.get_user_id() == user_id:
                bookings_of_user.append(elem)
                # print(elem, 'Step 2')
        '''Check ob es Einträge gibt, ansonsten return 0 '''
        if len(bookings_of_user) >= 1:
            '''Von den Bookings werden diejenigen selektiert, die Timeintervalle beinhalten'''
            for elem in bookings_of_user:
                # print('in bookins_of_user: ', elem)
                ev_b_id = elem.get_event_booking_id()
                ev_b = self.get_event_booking_by_id(ev_b_id)
                event_booking_of_user.append(ev_b)
                # for elem in timeinterval_booking_of_user:
                    # print(elem, 'Step 3')
            '''Von den Bookings des Users werden die Ids für die Timeintervalle abgelesen und diese aus der Datenbank
               geleaden.'''
            for elem in event_booking_of_user:
                # print('in ti_b for user: ', elem)
                ev_id = elem.get_event_id()
                ev = self.get_event_by_id(ev_id)
                events_of_user.append(ev)
            '''Von den Zeitintervallen werden diejenigen selektiert, die als Typ projectwork besitzen'''
            for elem in events_of_user:
                print(elem.get_type(), 'Step 4')
                if elem.get_type() == 'vacationEnd':
                    vacation = self.get_vacation_end_by_id(
                        elem.get_vacation_end_id())
                    all_events.append(vacation)
                if elem.get_type() == 'vacationBegin':
                    vacation = self.get_vacation_begin_by_id(
                        elem.get_vacation_begin_id())
                    all_events.append(vacation)
                if elem.get_type() == 'breakBegin':
                    break_bo = self.get_break_begin_by_id(
                        elem.get_break_begin_id())
                    all_events.append(break_bo)
                if elem.get_type() == 'breakEnd':
                    break_bo = self.get_break_end_by_id(
                        elem.get_break_end_id())
                    all_events.append(break_bo)
                if elem.get_type() == 'illnessBegin':
                    illnessbegin = self.get_illness_begin_by_id(
                        elem.get_illness_begin_id())
                    all_events.append(illnessbegin)
                if elem.get_type() == 'illnessEnd':
                    illnessend = self.get_illness_end_by_id(
                        elem.get_illness_end_id())
                    all_events.append(illnessend)
                if elem.get_type() == 'flexDayStart':
                    flexdaystart = self.get_flex_day_start_by_id(
                        elem.get_flex_day_start_id())
                    all_events.append(flexdaystart)
                if elem.get_type() == 'flexDayEnd':
                    flexdayend = self.get_flex_day_end_by_id(
                        elem.get_flex_day_end_id())
                    all_events.append(flexdayend)
                if elem.get_type() == 'projectWorkBegin':
                    project_work_begin = self.get_project_work_begin_by_id(
                        elem.get_project_work_begin_id())
                    all_events.append(project_work_begin)
                if elem.get_type() == 'projectWorkEnd':
                    project_work_end = self.get_project_work_end_by_id(
                        elem.get_project_work_end_id())
                    all_events.append(project_work_end)
                if elem.get_type() == 'coming':
                    coming = self.get_coming_by_id(
                        elem.get_coming_id())
                    all_events.append(coming)
                if elem.get_type() == 'going':
                    going = self.get_going_by_id(
                        elem.get_going_id())
                    all_events.append(going)
            
        return all_events




    def get_user_by_coming_id(self, coming):
        """
        @author Khadidja Kebaili (https://github.com/Khadidja-Kebaili)

        Diese Methode gibt den WorkTimeAccount zurück, durch die Angabe einer Coming-Id.
        :param coming: ComingBOId
        :return: Worktimeaccount
        """

        'Alle Timeintervals, Timerinterval-Buchungen und Buchungen'
        all_bookings_type_event = self.get_all_bookings_for_events()
        all_id_event_in_bookings = []

        'Dies sind die Userspezifischen Bookings, Timeintervalle und deren Subklassen'
        event_bookings = []
        event_id = []

        '''In diesem Schritt werden von den BookingBOs diejenigen selektiert, die dem User zugeordnet werden.'''
        for elem in all_bookings_type_event:
            all_id_event_in_bookings.append(elem.get_event_booking_id())
        '''Check ob es Einträge gibt, ansonsten return 0 '''
        if len(all_id_event_in_bookings) >= 1:
            '''Von den Bookings werden diejenigen selektiert, die Timeintervalle beinhalten'''
            for elem in all_id_event_in_bookings:
                print(elem, 'step 2')
                event_booking = self.get_event_booking_by_id(elem)
                event_bookings.append(event_booking)

        events = self.get_all_events()
        for elem in events:
            if elem.get_coming_id() == coming:
                event_id.append(elem.get_id())
        for elem in all_bookings_type_event:
            for x in event_bookings:
                if elem.get_event_booking_id() == x.get_id():
                    return elem.get_work_time_account_id()

    def get_projects_of_user(self, userid):
        # @author Ha Mi Duong (https://github.com/HamiDuong)
        # holt mit der UserId alle zugehörigen ProjectUserBO und nutzt diese um die entsprechenden Projekte zu holen
        projectuser = self.get_project_user_by_user_id(userid)
        projectid = []
        for elem in projectuser:
            projectid.append(elem.get_project_id())
        res = []
        for elem in projectid:
            hold = self.get_project_by_id(elem)
            res.append(hold)
        return res

    def in_between_times(self, searched_time, start, end):
        """
        Hilfsfunktion.
        Checkt ob sich eine gesuchte Zeit innerhalb einer Zeitspanne befinden.
        :param searched_time: Zeit, die gesucht wird
        :param start: Beginn Zeitspanne
        :param end: Ende der Zeitspanne
        :return: Boolean Wert, True wenn es sich in der Zeitspanne befindet, False wenn nicht.
        """
        searched_time = searched_time.strftime('%Y-%m-%d')
        start = datetime.strptime(start, '%Y-%m-%d')
        start = start.strftime('%Y-%m-%d')
        end = datetime.strptime(end, '%Y-%m-%d')
        end = end.strftime('%Y-%m-%d')
        if start <= searched_time <= end:
            return True
        else:
            return False

adm = Businesslogic()
print(adm.get_actual_working_time_for_user_by_activity_id(1,2))