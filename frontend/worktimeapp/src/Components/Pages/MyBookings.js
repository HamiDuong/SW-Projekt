import React, {Component} from 'react';
import { 
    FormControl, 
    Box,
    Button,
    FormControlLabel,
    Radio,
    FormLabel,
    RadioGroup,
    TextField,
    InputLabel,
    MenuItem,
    Select,
    TableCell,
    Paper,
    TableContainer,
    Table,
    TableHead,
    TableRow,
    TableBody,
    paperClasses
} from '@mui/material';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import EditBooking from '../Dialog/EditBooking';
import MyBookingsIntervalEntry from '../MyBookingsIntervalEntry';
import MyBookingsEventEntry from '../MyBookingsEventEntry';
import CreateTimeWorkSheet from '../Dialog/CreateTimeWorkSheet';

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

const fakebackend = {
    "timeintervals": [
        {
            "start": "2022-05-30 08:00:00",
            "end":"2022-05-30 18:30:00",
            "start_event": 1,
            "end_event": 2,
            "type": "Work",
            "id": 19,
            "date_of_last_change":"2022-05-30 18:30:00"
        },
        {
            "start":"2022-05-30 12:00:00",
            "end":"2022-05-30 12:30:00",
            "start_event": 3,
            "end_event": 4,
            "type": "Break",
            "id": 20,
            "date_of_last_change":"2022-05-30 "
        },
        {
            "start":"2022-05-30 15:00:00",
            "end":null,
            "start_event": null,
            "end_event": null,
            "type": "Break",
            "id": 21,
            "date_of_last_change":"2022-05-30 15:00:00"
        }
    ],
    "events":[
        {
            "time": "2022-05-30 8:00:00",
            "type": "coming",
            "id": 1,
            "date_of_last_change": "2022-05-30 08:00:00"
        },
        {
            "time": "2022-05-30 18:00:00",
            "type": "going",
            "id": 2,
            "date_of_last_change": "2022-05-30 18:00:00"
        },
        {
            "time": "2022-05-30 12:00:00",
            "type": "breakbegin",
            "id": 3,
            "date_of_last_change": "2022-05-30 12:00:00"
        },
        {
            "time": "2022-05-30 12:30:00",
            "type": "breakend",
            "id": 4,
            "date_of_last_change": "2022-05-30 12:30:00"
        }        
    ]
}

/**
 * Auflistung aller Buchungen des aktiven Users
 * 
 * @author [Ha Mi Duong] (https://github.com/HamiDuong)
 */

class MyBookings extends Component {
    constructor(props){
        super(props);
        this.state = {
            userId : props.userId,

            intervalbookings: [],
            eventbookings: [],

            filteredintervalbookings: [],
            filteredeventbookings: [],

            workbookings: [],

            bookingtype: 'all',
            typefilter: null,
            startfilter: null,
            endfilter: null,

            loadingInProgress: false,
            showResetButton: true,
            showFilterButton: false,
            error: null,

            dialogWorkTimeSheet: false,
            showEditWindow: false
        }
    }

    componentDidMount(){
        console.log('ComponentDidMount');
        this.getBookings();
        this.getWorkBookings();
        console.log("userid bookings", this.props.userId);
        //this.getWorkBookings();
    }

    // componentDidUpdate(prevProps){
    //     if ((this.props.show) && (this.props.show !== prevProps.show)) {
    //         this.getBookings();
    //       }        
    // }

    handleChange = ev => {
        this.setState({ [ev.target.name] : ev.target.value });
    };

    //gets all booked bookings of the current user
    getBookings = () => {
        // WorkTimeAppAPI.getAPI().getAllBookingsForUser(this.props.userId).then(responseJSON =>
        //     this.setState({
        //         intervalbookings: responseJSON.timeintervals,
        //         eventbookings: responseJSON.events,
        //         filteredintervalbookings: responseJSON.timeintervals,
        //         filteredeventbookings: responseJSON.events            
        //     },function(){
        //         console.log("getBookings");
        //     }))
                
            this.setState({
                    intervalbookings: fakebackend.timeintervals,
                    eventbookings: fakebackend.events,
                    filteredintervalbookings: fakebackend.timeintervals,
                    filteredeventbookings: fakebackend.events            
                },function(){
                    console.log("getBookings");
                });

            //filtert intervalbookings with the type 'Work'
            let res = [];
            let bookings = fakebackend.timeintervals;
            bookings.forEach(elem => {
                if(elem.type == "Work"){
                    res.push(elem);
                }
            });
            this.setState({
                workbookings: res
            }, function(){
                console.log("Workbookings wurden ausgefiltert")
            });
    }

    //filtert intervalbookings with the type 'Work'
    getWorkBookings = () => {
        let res = [];
        let bookings = this.state.intervalbookings;
        bookings.forEach(elem => {
            if(elem.type == "Work"){
                res.push(elem);
                console.log(elem.type);
            }
        });
        this.setState({
            workbookings: res
        }, function(){
            console.log("Workbookings wurden ausgefiltert");
        });
    }

    //reset the filter to default
    resetFilter = () => {
        this.setState({
            bookingtype: 'all',
            typefilter: '',
            startfilter: null,
            endfilter: null,
            showResetButton: true,
            showFilterButton: false,
            filteredintervalbookings: this.state.intervalbookings,
            filteredeventbookings: this.state.eventbookings
        }, function(){
            console.log("State wurde zurückgesetzt");
        })
    }

    //sortes through all bookings according to the set filters
    filterBookings = () => {
        let starthold = document.getElementById("startfilter");
        let endhold = document.getElementById("endfilter");
        let type = this.state.typefilter;

        this.setState({
            startfilter: starthold.value,
            endfilter: endhold.value,
            showResetButton: false,
            showFilterButton: true
        }, function(){
            console.log("Zeitfilter wurden gesetzt");
        });

        //Holder for result of filter
        let ires = [];
        let eres = [];

        //Filter bookings by type
        //Filter event bookings by type
        if(type == null || type == ""){
            console.log("Keine Typefilterung")
        }else{
            this.state.filteredintervalbookings.forEach(function(elem){
                let elemtype = elem.type;

                // Event types
                if(elemtype == "breakbegin" || elemtype == "breakend"){
                    elemtype = "Break";
                }else if(elemtype == "coming" || elemtype == "going"){
                    elemtype = "Work";
                }else if(elemtype == "flexdayend" || elemtype == "flexdaystart"){
                    elemtype = "Flex Day";
                }else if(elemtype == "illnessbegin" || elemtype == "illnessend"){
                    elemtype = "Illness";
                }else if(elemtype == "projectworkbegin" || elemtype == "projectworkend"){
                    elemtype = "Project Work";
                }else if(elemtype == "vacationbegin" || elemtype == "vacationend"){
                    elemtype = "Vacation";
                }

                if(type == elemtype){
                    ires.push(elem);
                    console.log('Element gehört in den Filter');
                }else{
                    console.log('Element gehört nicht in das Filter');
                }

            })

            this.setState({
                filteredintervalbookings: ires
            }, function(){
                console.log("State wurde gesetzt für IntervalBuchungen nach TypeFilterung");
            });
        }

        //Filter interval bookings by type
        if(type == null || type == ""){
            console.log("Keine Typfilterung");
        }else{
            this.state.filteredeventbookings.forEach(function(elem){
                let elemtype = elem.type;
                console.log(elemtype);
                if(type == elemtype){
                    eres.push(elem);
                    console.log('Elemt gehört in den Filter');
                }else{
                    console.log('Element gehört nicht in das Filter');
                }
            });
            this.setState({
                filteredeventbookings: eres
            }, function(){
                console.log("State wurde gesetzt für EventBuchungen nach TypeFilterung");
            })
        }

        //Sort Interval by Date
        ires = [];

        let starttime = starthold.value;
        let endtime = endhold.value;
        if(starttime == "" && endtime == ""){
            console.log("No time filter");
        }else if(starttime != "" && endtime == ""){
            let startdate = new Date(starttime);
            console.log("Interval sorted by start date: "+startdate);

            this.state.filteredintervalbookings.forEach(function(elem){
                let elemstarttime = new Date(elem.start);
                if(elemstarttime >= startdate){
                    ires.push(elem);
                }
            })
            this.setState({
                filteredintervalbookings: ires
            }, function(){
                console.log("Finished sorting by start date");
            })
        }else if(starttime != "" && endtime == ""){
            let enddate = new Date(endtime);
            console.log("Endfilter wurde gesetzt mit: "+enddate);
        
            this.state.filteredintervalbookings.forEach(function(elem){
                let elemendtime = new Date(elem.end);
                if(elemendtime <= enddate){
                    ires.push(elem);
                }
            })
            this.setState({
                filteredintervalbookings: ires
            }, function(){
                console.log("Interval sorted by end date");
            })
        }else{
            let startdate = new Date(starttime);
            let enddate = new Date(endtime);

            this.state.filteredintervalbookings.forEach(function(elem){
                let elemstarttime = new Date(elem.start);
                let elemendtime = new Date(elem.end);
                if(elemendtime <= enddate && elemstarttime >= startdate){
                    ires.push(elem);
                }
            })
            this.setState({
                filteredintervalbookings: ires
            }, function(){
                console.log("Interval sorted by start and end date");
            })
            
        }

        //Sort events by time
        eres = [];
        if(starttime == ""){
            console.log("No start time filter");
        }else{
            let etime = new Date(starttime);
            console.log("Start filter is: "+etime);

            this.state.filteredeventbookings.forEach(function(elem){
                let eventtime = new Date(elem.time);
                if(eventtime >= etime){
                    eres.push(elem);
                }
            })
            this.setState({
                filteredeventbookings: eres
            }, function(){
                console.log("Event sorted by start date");
            })
        }

        let bookingtype = this.state.bookingtype;
        let timeinterval = 'timeinterval';
        let event = 'event';

        console.log('Vergleich von Buchungsart');
        if(bookingtype == timeinterval){
            this.setState({
                filteredeventbookings: []
            },function(){
                console.log("Nur Timeintervalbuchungen");
            })
        }else if(bookingtype == event){
            this.setState({
                filteredintervalbookings: []
            }, function(){
                console.log("Nur Eventbuchungen");
            })
        }
    }
    
    editRow = (event) => {
        event.stopPropagation();
        this.setState({
            showEditWindow: true
        },function(){
            console.log("Editwindow wird geöffnet");
        });
    }

    mapIntervalBookings = () => {
        return(
            <TableBody>
                {
                    this.state.filteredintervalbookings.map( row => <MyBookingsIntervalEntry booking={row} userId={this.props.userId}/>)
                }
            </TableBody>
        )
    }

    mapEventBookings = () => {
        return(
            <TableBody>
                {
                    this.state.filteredeventbookings.map( row => <MyBookingsEventEntry booking={row} userId={this.props.userId}/>)
                }
            </TableBody>
        )
    }

    //Check state of component
    printState = () => {
        console.log(this.state.intervalbookings);
        console.log(this.state.eventbookings);
        console.log(this.state.bookingtype);
        console.log(this.state.typefilter);
        console.log(this.state.startfilter);
        console.log(this.state.endfilter);
        console.log(this.state.showEditWindow);
    }

    openCreateWorkTimeSheet = () => {
        this.setState({
            dialogWorkTimeSheet: true
        },function(){
            console.log("Open Create WorkTimeSheet Window");
        })
    }

    //TODO
    closeDialog = () => {
        this.setState({
            dialogWorkTimeSheet: false
        }, function(){
            console.log("Editwindow wird geschlossen");
        })
    }

    render(){
        return(
            <>
                {/* <h1>My Bookings</h1> */}
                <div>
                    <h2>Filter Settings</h2>
                    <FormControl>
                        <FormLabel id="viewfilter"></FormLabel>
                        <RadioGroup
                            row
                            name= 'bookingtype'
                            defaultValue="all"
                            onChange={this.handleChange}
                            value={this.state.bookingtype}
                        >
                            <FormControlLabel value="all" control={<Radio />} label="Show all" />
                            <FormControlLabel value="timeinterval" control={<Radio />} label="Only Time Interval Bookings" />
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
                        type = "date"
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <TextField
                        id="endfilter"
                        label="End Date"
                        variant="standard"
                        format={'YYYY/MM/DD'}
                        type = "date"
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <FormControl sx={{ minWidth: 258}}>
                        <InputLabel>Type</InputLabel>
                        <Select
                        name='typefilter'
                        value={this.state.typefilter}
                        onChange={this.handleChange}
                        variant="standard"
                        >
                            <MenuItem value={"Work"}>Work</MenuItem>
                            <MenuItem value={"Flex Day"}>Flex Day</MenuItem>
                            <MenuItem value={"Sick Day"}>Sick Day</MenuItem>
                            <MenuItem value={"Vacation"}>Vacation</MenuItem>
                            <MenuItem value={"Break"}>Break</MenuItem>
                            <MenuItem value={"Project Work"}>Project Work</MenuItem>
                        </Select>
                    </FormControl>
                    <Button
                        onClick={this.filterBookings}
                        disabled = {this.state.showFilterButton}
                    >
                        Filter Results
                    </Button>
                    <Button
                        disabled = {this.state.showResetButton}
                        onClick={this.resetFilter}
                    >
                        Remove Filter
                    </Button>
                    {/* <Button
                        onClick={this.printState}
                    >
                        Print State
                    </Button> */}
                    <Button
                        onClick={this.openCreateWorkTimeSheet}
                    >
                        Create Work Time Sheet
                    </Button>
                </Box>
                <Box sx={{width: '100%'}}>
                    <h2>My Bookings</h2>
                    <Paper sx={{width: '100%', mb: 2}}>
                        <TableContainer>
                            <Table>
                                <TableHead>
                                    <TableRow>
                                        {header.map((headcell) => (
                                            <TableCell
                                                key = {headcell.id}
                                                padding={headcell.disablePadding ? 'none' : 'normal'}

                                            >
                                                {headcell.name}

                                            </TableCell>
                                        ))}
                                    </TableRow>
                                </TableHead>
                                <this.mapIntervalBookings></this.mapIntervalBookings>
                                <this.mapEventBookings></this.mapEventBookings>
                            </Table>
                        </TableContainer>
                    </Paper>
                </Box>
                <CreateTimeWorkSheet show = {this.state.dialogWorkTimeSheet} workbookings = {this.state.workbookings} onClose={this.closeDialog} userId = {this.state.userId}></CreateTimeWorkSheet>
            </>
        );
    }
}
 
export default MyBookings;