import React, { Component } from 'react';
import {
    FormControl,
    Box,
    Button,
    FormControlLabel,
    Radio,
    FormLabel,
    RadioGroup,
    TextField,
    TableCell,
    Paper,
    TableContainer,
    Table,
    TableHead,
    TableRow,
    TableBody,
} from '@mui/material';
import MyBookingsIntervalEntry from '../MyBookingsIntervalEntry';
import MyBookingsEventEntry from '../MyBookingsEventEntry';
import CreateTimeWorkSheet from '../Dialog/CreateTimeWorkSheet';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';

// header cells for booking table
const header = [
    {
        id: 'bookingtype',
        name: 'Booking Type',
        numeric: false,
        disablePadding: false,
        label: 'Event/ Interval'
    },
    {
        id: 'type',
        name: 'Type',
        numeric: false,
        disablePadding: false,
        label: 'Type'
    },
    {
        id: 'start',
        name: 'Start Date',
        numeric: true,
        disablePadding: false,
        label: 'Start Date'
    },
    {
        id: 'end',
        name: 'End Date',
        numeric: true,
        disablePadding: false,
        label: 'End Date'
    }
]


/**
 * @author [Ha Mi Duong] (https://github.com/HamiDuong)
 * 
 * All bookings of the current user in a table
 */
class MyBookings extends Component {
    constructor(props) {
        super(props);
        this.state = {
            userId: props.userId,
            showDialog: false,

            intervalbookings: [],
            eventbookings: [],

            filteredintervalbookings: [],
            filteredeventbookings: [],

            eventbookings2: [],
            filteredeventbookings2: [],

            workbookings: [],

            bookingtype: 'timeinterval',
            typefilter: null,
            startfilter: null,
            endfilter: null,

            loadingInProgress: false,
            showResetButton: true,
            showFilterButton: false,
            error: null,

            holdintervalbooking : null,
            holdeventbooking : null,
            holdeventbooking2 : null,

            dialogWorkTimeSheet: false,
            showEditWindow: true
        }
    }

    // After component mounted following function will be executed: the booked bookings of the user and the work bookings will be saved in state
    componentDidMount() {
        console.log('ComponentDidMount');
        this.getBookings();
    }

    // componentDidUpdate(prevProps, prevState) {
    //     //let length = this.state.intervalbookings.length

    //     if(this.state.showResetButton == false){
    //         console.log("Filterung aktiv")
    //     }else{
    //         // only update if searchValue has changed
    //         if (prevState.eventbookings2 !== this.state.eventbookings2 || prevState.intervalbookings !== this.state.intervalbookings ||
    //             prevState.intervalbookings.length !== this.state.intervalbookings.length || prevState.eventbookings !== this.state.eventbookings ||
    //             prevState.filteredeventbookings !== this.state.filteredeventbookings) {
    //             console.log('ComponentDidMount');
    //             this.getBookings();
    //             this.getWorkBookings();
    //         }            
    //     }
    //     // // only update if searchValue has changed
    //     // if (prevState.eventbookings2 !== this.state.eventbookings2 || prevState.intervalbookings !== this.state.intervalbookings ||
    //     //     prevState.intervalbookings.length !== this.state.intervalbookings.length || prevState.eventbookings !== this.state.eventbookings ||
    //     //     prevState.filteredeventbookings !== this.state.filteredeventbookings) {
    //     //     console.log('ComponentDidMount');
    //     //     this.getBookings();
    //     //     this.getWorkBookings();
    //     // }
    // }

    // Save changes buttons and textfields into state
    handleChange = ev => {
        this.setState({ [ev.target.name]: ev.target.value });
    };

    // filterBookings = () => {
    //     let bookings = this.props.intervalbookings;
    //     let res = [];

    //     bookings.forEach(element => {
    //         if (element.type == "Work") {
    //             res.push(element);
    //         }
    //     });

    //     this.setState({
    //         intervalbookings: res
    //     }, function () {
    //         console.log("Gefiltert")
    //     })

    // }

    // Gets all booked bookings of the current user
    getBookings = () => {
        WorkTimeAppAPI.getAPI().getAllBookingsForUser(this.props.userId).then(responseJSON =>
            this.setState({
                intervalbookings: responseJSON.timeintervals,
                eventbookings: responseJSON.events,
                filteredintervalbookings: responseJSON.timeintervals,
                filteredeventbookings: responseJSON.events
            }, function () {
                let work = responseJSON.timeintervals;
                let res = [];

                work.forEach(element => {
                    if (element.type == "Work") {
                        res.push(element);
                    }
                });
                this.setState({
                    workbookings: res
                }, function () {
                    console.log("Workbookings filtern");
                    console.log(this.state.workbookings);
                })

            }))

        WorkTimeAppAPI.getAPI().getVacationIllnessEventBookings(this.props.userId).then(vacationBOs =>
            this.setState({
                eventbookings2: vacationBOs,
                filteredeventbookings2 : vacationBOs
            }, function () {
                console.log(this.state.eventbookings2);
            }))

    }

    // Filter intervalbookings with the type 'Work'
    getWorkBookings = () => {
        let res = [];
        let bookings = this.state.intervalbookings;

        bookings.forEach(elem => {
            if (elem.type == "Work") {
                res.push(elem);
                console.log(elem.type);
            }
        });
        this.setState({
            workbookings: res
        }, function () {
            console.log("Workbookings wurden ausgefiltert");
        });
    }

    // Reset the filter to default
    resetFilter = () => {
        this.setState({
            bookingtype: 'timeinterval',
            typefilter: '',
            // startfilter: null,
            // endfilter: null,
            showResetButton: true,
            showFilterButton: false,
            filteredintervalbookings: this.state.intervalbookings,
            filteredeventbookings: this.state.eventbookings,
            filteredeventbookings2 : this.state.eventbookings2
        }, function () {
            console.log("State wurde zurÃ¼ckgesetzt");
        })
    }

    closeEventEditDialog = booking => {
        console.log(booking)
        if (booking) {
            const newBookingList = [booking];
            this.setState({
                eventbookings2: newBookingList,
                filteredeventbookings: [...newBookingList],
                showDialog: false
            }, function () {
                console.log("Editwindow wird geschlossen")
            })
        } else {
            this.setState({
                showDialog: false
            }, function () {
                console.log("Editwindow wird geschlossen ohne Update")
            })

        }
    }

    closeEditDialog = booking => {
        console.log(booking)
        if (booking) {
            const newBookingList = [booking];
            this.setState({
                intervalbookings: newBookingList,
                filteredintervalbookings: [...newBookingList],
                showDialog: false
            }, function () {
                console.log("Editwindow wird geschlossen")
            })
        } else {
            this.setState({
                showDialog: false
            }, function () {
                console.log("Editwindow wird geschlossen ohne Update")
            })

        }
    }

    // Map table rows for interval bookigns
    mapIntervalBookings = () => {
        return (
            <TableBody>
                {
                    this.state.filteredintervalbookings.map(row => <MyBookingsIntervalEntry key = {row.id + " " + row.type} onClose1={this.closeEditDialog} booking={row} userId={this.props.userId} />)
                }
            </TableBody>
        )
    }

    // Map table rows for event bookings
    mapEventBookings = () => {
        return (
            <TableBody>
                {
                    this.state.filteredeventbookings.map(row => <MyBookingsEventEntry key = {row.id + " " + row.type+ "1" } onClose1={this.closeEventEditDialog} booking={row} userId={this.props.userId} />)
                }
                {/* {
                    this.state.filteredeventbookings2.map(row => <MyBookingsEventEntry key = {row.id + " " + row.type+ "2"} onClose1={this.closeEventEditDialog} booking={row} userId={this.props.userId} />)
                } */}
            </TableBody>
        )
    }

    //Callback Funktion to confirm when forEach is finished
    callBack(){
        console.log("Fertig");
    }

    // Sortes through all bookings according to the set filters
    filterBookings = () => {
        let starthold = document.getElementById("startfilter");
        let endhold = document.getElementById("endfilter");

        this.setState({
            startfilter: starthold.value,
            endfilter: endhold.value,
            showResetButton: false,
            showFilterButton: true
        }, function () {
            console.log("Zeitfilter wurden gesetzt");
        });

        console.log("Buchungen ohne Änderungen");
        console.log("INterval",this.state.intervalbookings);
        console.log("event",this.state.eventbookings);
        console.log("event2",this.state.eventbookings2);

        WorkTimeAppAPI.getAPI().getAllTimeIntervalsWithinTimeFrame(this.state.userId, starthold.value, endhold.value).then(responseInterval => 
            this.setState({
                filteredintervalbookings : responseInterval
            }, function(){
                console.log("Got Intervalbookings")
            })    
        )

        WorkTimeAppAPI.getAPI().getAllEventsWithinTimeFrame(starthold.value, endhold.value).then(responseEvents =>
            this.setState({
                filteredeventbookings : responseEvents
            }, function(){
                console.log("Gor Eventbookings")
            })    
        )

        // let icounter = this.state.intervalbookings.length;
        // let ecounter = this.state.eventbookings.length;
        // let ecounter2 = this.state.eventbookings2.length;

        // // Sort interval bookings by date
        // let starttime = starthold.value;
        // let endtime = endhold.value;

        // // No filter
        // console.log("verleich kein", starttime == "" && endtime == "")
        // if (starttime == "" && endtime == "") {
        //     console.log("No time filter");

        // // Only Start filter  
        // } else if (starttime != "" && endtime == "") {
        //     let ires = [];
        //     let counter = 0;
        //     let startdate = new Date(starttime);
        //     console.log("Interval sorted by start date: " + startdate);

        //     this.state.filteredintervalbookings.forEach((elem) => {
        //         console.log("Element", elem)
        //         let elemstarttime = new Date(elem.start);
        //         console.log("wird es gepusht", elemstarttime >= startdate);
        //         if (elemstarttime >= startdate) {
        //             ires.push(elem);
        //             counter++;
        //         }else{
        //             console.log("Element rausgefiltert");
        //             counter++;
        //         }

        //         if(counter == icounter){
        //             this.callBack();
        //         }
        //     })
        //     this.setState({
        //         filteredintervalbookings: ires
        //     }, function () {
        //         console.log("Finished sorting by start date", this.state.filteredintervalbookings);
        //     })

        // // Only End filter
        // } else if (starttime != "" && endtime == "") {
        //     let ires = [];
        //     let counter = 0;
        //     console.log("Nur Endfilter", starttime != "" && endtime == "" );
        //     let enddate = new Date(endtime);
        //     console.log("Endfilter wurde gesetzt mit: " + enddate);

        //     this.state.filteredintervalbookings.forEach((elem) => {
        //         console.log("Element, ", elem);
        //         let elemendtime = new Date(elem.end);
        //         if (elemendtime <= enddate) {
        //             console.log("wird es gepusht", elemendtime <= enddate);
        //             ires.push(elem);
        //             counter++;
        //         }else{
        //             console.log("Element raus")
        //             counter++;
        //         }

        //         if(counter === icounter){
        //             this.callBack();
        //         }
        //     })
        //     this.setState({
        //         filteredintervalbookings: ires
        //     }, function () {
        //         console.log("Interval sorted by end date", this.state.filteredintervalbookings);
        //     })

        // // Start and End Filter
        // } else {
        //     let ires = [];
        //     let counter = 0;
        //     let startdate = new Date(starttime);
        //     let enddate = new Date(endtime);

        //     this.state.filteredintervalbookings.forEach((elem) => {
        //         let elemstarttime = new Date(elem.start);
        //         let elemendtime = new Date(elem.end);

        //         if (elemendtime <= enddate && elemstarttime >= startdate) {
        //             ires.push(elem);
        //             console.log("ires", ires)
        //             counter++;

        //         }else{
        //             console.log("Element passt nicht");
        //             console.log("ires", ires);
        //             counter++;
        //         }

        //         if(counter === icounter){
        //             this.callBack();
        //         }
        //     })
        //     this.setState({
        //         filteredintervalbookings: ires,
        //     }, function () {
        //         console.log("Interval sorted by start and end date", ires);
        //     })
        // }

        // // Sort event bookings with timeintervals by time

        // // No filter
        // if (starttime == "" && endtime == "") {
        //     console.log("No start time filter");

        // // Start filter
        // } else if(starttime != "" && endtime == ""){
        //     let eres = [];
        //     let eres2 = []
        //     let counter = 0;
        //     let etime = new Date(starttime);
        //     console.log("Start filter is: " + etime);

        //     this.state.filteredeventbookings.forEach((elem) => {
        //         let eventtime = new Date(elem.time);
        //         if (eventtime >= etime) {
        //             eres.push(elem);
        //             counter++;
        //         }else{
        //             counter++;
        //             console.log("Element raus")
        //         }

        //         if(ecounter === counter){
        //             this.callBack();
        //         }
        //     })
        //     this.setState({
        //         filteredeventbookings: eres
        //     }, function () {
        //         console.log("Event sorted by start date");
        //     })

        //     this.state.filteredeventbookings2.forEach((elem) => {
        //         let counter2 = 0;
        //         let eventtime2 = new Date(elem.time);
        //         if(eventtime2 >= etime){
        //             eres2.push(elem)
        //             counter2++;
        //         }else{
        //             console.log("Element raus");
        //             counter2++;
        //         }

        //         if(counter2 == ecounter2){
        //             this.callBack();
        //         }
        //     })
        //     this.setState({
        //         filteredeventbookings2 : eres2
        //     }, function(){
        //         console.log("Event2 sorted by start date");
        //     })

        // // Endfilter
        // } else if (starttime == "" && endtime != ""){
        //     let eres = [];
        //     let eres2 = [];
        //     let counter2 = 0;
        //     let etime = new Date(endtime);
        //     console.log("End filter is: " + etime);

        //     this.state.filteredeventbookings.forEach((elem) => {
        //         let eventtime = new Date(elem.time);
        //         if (eventtime <= etime) {
        //             eres.push(elem);
        //             counter2++;
        //         }else{
        //             counter2++;
        //             console.log("Element raus");
        //         }

        //         if(ecounter2 === counter2){
        //             this.callBack();
        //         }
        //     })
        //     this.setState({
        //         filteredeventbookings: eres
        //     }, function () {
        //         console.log("Event sorted by start date");
        //     })

        //     this.state.filteredeventbookings2.forEach((elem) => {
        //         let counter2 = 0;
        //         let eventtime2 = new Date(elem.time);
        //         if(eventtime2 <= etime){
        //             eres2.push(elem);
        //             counter2++;
        //         }else{
        //             console.log("Element raus");
        //             counter2++;
        //         }

        //         if(counter2 == ecounter2){
        //             this.callBack();
        //         }
        //     })
        //     this.setState({
        //         filteredeventbookings2 : eres2
        //     }, function(){
        //         console.log("Event2 sorted by start date");
        //     })

        // // Start und End Filter
        // } else if (starttime != "" && endtime != ""){
        //     let eres = [];
        //     let erestwo = [];
        //     let counter = 0;
        //     let etime = new Date(endtime);
        //     let stime = new Date(starttime);

        //     this.state.filteredeventbookings.forEach((elem) => {
        //         let eventtime = new Date(elem.time);
        //         if (eventtime <= etime && eventtime >= stime) {
        //             eres.push(elem);
        //             counter++;
        //         }else{
        //             counter++;
        //             console.log("Element raus");
        //         }

        //         if(ecounter === counter){
        //             this.callBack();
        //         }
        //     })
        //     this.setState({
        //         filteredeventbookings: eres
        //     }, function () {
        //         console.log("Event sorted by start date");
        //     })

        //     this.state.filteredeventbookings2.forEach((elem) => {
                
        //         let counter2 = 0;
        //         let eventtime2 = new Date(elem.time);
        //         if(eventtime2 <= etime && eventtime2 >= stime){
        //             erestwo.push(elem);
        //             counter2++;
        //         }else{
        //             console.log("Element raus");
        //             counter2++;
        //         }

        //         if(counter2 == ecounter2){
        //             this.callBack();
        //         }
        //     })
        //     this.setState({
        //         filteredeventbookings2 : erestwo
        //     }, function(){
        //         console.log("Event2 sorted by start date");
        //     })
        // }

        // // Filter by booking type
        // let bookingstype = this.state.bookingtype

        // console.log('Vergleich von Buchungsart');
        // if (bookingstype == 'timeinterval') {
        //     this.setState({
        //         eventbookings2 : []
        //     }, function () {
        //         console.log("Nur Timeintervalbuchungen mit verknüpften Events");
        //     })
        // } else if (bookingstype == 'event') {
        //     this.setState({
        //         filteredintervalbookings: [],
        //         filteredeventbookings: [],
        //     }, function () {
        //         console.log("Nur Eventbuchungen");
        //     })
        // }
    }




    // Check state of component (for debuggin)
    printState = () => {
        console.log(this.state.intervalbookings);
        console.log(this.state.eventbookings);
        console.log(this.state.bookingtype);
        console.log(this.state.typefilter);
        console.log(this.state.startfilter);
        console.log(this.state.endfilter);
        console.log(this.state.showEditWindow);
    }

    // open the dialog window for work time sheet
    openCreateWorkTimeSheet = () => {
        this.setState({
            dialogWorkTimeSheet: true
        }, function () {
            console.log("Open Create WorkTimeSheet Window");
        })
    }

    // close the dialog window for work time sheet
    closeDialog = () => {
        this.setState({
            dialogWorkTimeSheet: false
        }, function () {
            console.log("Editwindow wird geschlossen");
        })
    }

    // render the component
    render() {
        const { workbookings } = this.state;
        return (
            <>
                {/* <h1>My Bookings</h1> */}
                <div>
                    <h2>Filter Settings</h2>
                    <FormControl>
                        <FormLabel id="viewfilter"></FormLabel>
                        <RadioGroup
                            row
                            name='bookingtype'
                            defaultValue="all"
                            onChange={this.handleChange}
                            value={this.state.bookingtype}
                        >
                            <FormControlLabel value="timeinterval" control={<Radio />} label="Time Interval with connected Events" />
                            <FormControlLabel value="event" control={<Radio />} label="Only Event Bookings" />
                        </RadioGroup>
                    </FormControl>
                </div>

                <Box
                    component="form"
                    sx={{
                        '& > :not(style)': { m: 1, width: '25ch' },
                    }}
                    noValidate
                    autoComplete="off"
                >
                    <TextField
                        id="startfilter"
                        label="Start Date"
                        variant="standard"
                        format={'YYYY/MM/DD'}
                        type="date"
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <TextField
                        id="endfilter"
                        label="End Date"
                        variant="standard"
                        format={'YYYY/MM/DD'}
                        type="date"
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <Button
                        onClick={this.filterBookings}
                        disabled={this.state.showFilterButton}
                    >
                        Filter Results
                    </Button>
                    <Button
                        disabled={this.state.showResetButton}
                        onClick={this.resetFilter}
                    >
                        Remove Filter
                    </Button>
                    <Button
                        onClick={this.openCreateWorkTimeSheet}
                    >
                        Create Work Time Sheet
                    </Button>
                </Box>
                <Box sx={{ width: '100%' }}>
                    <h2>My Bookings</h2>
                    <Paper sx={{ width: '100%', mb: 2 }}>
                        <TableContainer>
                            <Table>
                                <TableHead>
                                    <TableRow>
                                        {header.map((headcell) => (
                                            <TableCell
                                                key={headcell.id}
                                                padding={headcell.disablePadding ? 'none' : 'normal'}
                                            >
                                                {headcell.name}
                                            </TableCell>
                                        ))}
                                    </TableRow>
                                </TableHead>
                                <this.mapIntervalBookings />
                                <this.mapEventBookings />
                            </Table>
                        </TableContainer>
                    </Paper>
                </Box>
                <CreateTimeWorkSheet show={this.state.dialogWorkTimeSheet} workbookings={workbookings} onClose={this.closeDialog} userId={this.state.userId}></CreateTimeWorkSheet>
                {/* <MyBookingsIntervalEntry onClose1={this.closeEditDialog}></MyBookingsIntervalEntry> */}
            </>
        );
    }
}

export default MyBookings;