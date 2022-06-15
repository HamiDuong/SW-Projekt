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
            "start":"2022-05-30 08:00:00",
            "end":"2022-05-30 18:00:00",
            "start_event": 1,
            "end_event": 2,
            "type": "Work",
            "id": 19,
            "date_of_last_change":"2022-05-30 18:00:00"
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
            intervalbookings: [],
            eventbookings: [],

            filteredintervalbookings: [],
            filteredeventbookings: [],

            renderedbookings: [],

            bookingtype: 'all',
            typefilter: null,
            startfilter: null,
            endfilter: null,

            loadingInProgress: false,
            showResetButton: true,
            error: null,

            showEditWindow: false
        }
    }

    handleChange = ev => {
        this.setState({ [ev.target.name] : ev.target.value });
    };

    componentDidMount(){
        this.getBookings();
    }

    getBookings = () => {
        // hier muss Mihris Booking Methode rein um alle Buchungen eines Users zu holen
        this.setState({
            intervalbookings: fakebackend.timeintervals,
            eventbookings: fakebackend.events,
            filteredintervalbookings: fakebackend.timeintervals,
            filteredeventbookings: fakebackend.events            
        },function(){
            console.log("getBookings")
        })
    }

    resetFilter = () => {
        this.setState({
            bookingtype: 'all',
            typefilter: '',
            startfilter: null,
            endfilter: null,
            showResetButton: true
        }, function(){
            console.log(this.state.startfilter)
        })
    }

    printState = () => {
        console.log(this.state.intervalbookings);
        console.log(this.state.eventbookings);
        console.log(this.state.bookingtype);
        console.log(this.state.typefilter);
        console.log(this.state.startfilter);
        console.log(this.state.endfilter);
        console.log(this.state.showEditWindow);
    }

    filterBookings = () => {

        let starthold = document.getElementById("startfilter");
        let endhold = document.getElementById("endfilter");
        this.setState({
            startfilter: starthold.value,
            endfilter: endhold.value,
            showResetButton: false
        }, function(){
            console.log(this.state.startfilter);
        });

        let intervalbookings = this.state.intervalbookings;
        let eventbookings = this.state.eventbookings;
        let ires = [];
        let eres = [];

        //Intervalbookings nach Type filtern
        intervalbookings.forEach(function(elem){
            if(this.state.typefilter == elem.type){
                ires.push(elem)
            }else if(this.state.typefilter == elem.type){
                ires.push(elem)
            }else{
                console.log('Element gehört nicht in das Filter')
            }

        }, function(){
            this.setState({
                intervalbookings: ires
            }, function(){
                console.log("State wurde gesetzt für IntervalBuchungen nach TypeFilterung")
            })
        });

        // intervalbookings.forEach(function(elem){
        //     if(elem.start >= this.state.startfilter && elem.end <= this.state.endfilter){
        //         console.log(elem)
        //     }
        // })
        // console.log(ires);
    }

    renderIntervalBookings = () => {
        return(
            <TableBody>
                {this.state.filteredintervalbookings.map(row =>
                    <TableRow>
                        <TableCell>Interval</TableCell>
                        <TableCell>{row.type}</TableCell>
                        <TableCell>{row.start}</TableCell>
                        <TableCell>{row.end}</TableCell>
                        <TableCell>Remark</TableCell>
                    </TableRow>
                )}
            </TableBody>           
        )
    }

    renderEventBookings = () => {
        return(
            <TableBody>
                {this.state.filteredeventbookings.map(row =>
                    <TableRow>
                        <TableCell>Event</TableCell>
                        <TableCell>{row.type}</TableCell>
                        <TableCell>{row.time}</TableCell>
                        <TableCell>-</TableCell>
                        <TableCell>Remark</TableCell>
                    </TableRow>    
                )}
            </TableBody>            
        )
    }
    
    // filterBookings = () => {
    //     let start = this.state.startfilter;
    //     let end = this.state.endfilter;

    //     let holder = this.state.bookings;
    //     let res = [];

    //     holder.forEach(function(elem){
    //         console.log(elem);
    //         if(this.state.startfilter != null){

    //         }
    //     });

    //     this.setState({
    //         filteredbookings: res
    //     })
    // }

    editRow = (event) => {
        event.stopPropagation();
        this.setState({
            showEditWindow: true
        },function(){
            console.log("Editwindow wird geöffnet")
        })
    }

    render(){
        return(
            <div>
                <h1>My Bookings</h1>
                <div>
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
                    >
                        Filter Results
                    </Button>
                    <Button
                        disabled = {this.state.showResetButton}
                        onClick={this.resetFilter}
                    >
                        Remove Filter
                    </Button>
                    <Button
                        onClick={this.printState}
                    >
                        Print State
                    </Button>
                </Box>
                <Box sx={{width: '100%'}}>
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
                                <TableBody>
                                    {
                                        this.state.filteredintervalbookings.map( row => <MyBookingsIntervalEntry booking={row}/>)
                                    }

                                    {/* {this.state.filteredintervalbookings.map(row =>
                                        <TableRow
                                            hover
                                            onClick = {() => console.log("Click")}
                                        >
                                            <TableCell>Interval</TableCell>
                                            <TableCell>{row.type}</TableCell>
                                            <TableCell>{row.start}</TableCell>
                                            <TableCell>{row.end}</TableCell>
                                            <TableCell>Remark</TableCell>
                                        </TableRow>
                                    )} */}
                                </TableBody>
                                <TableBody>
                                    {/* {
                                        this.state.filteredeventbookings.map( row => <MyBookingsEventEntry key={row.getId()} booking={row}/>)
                                    } */}
                                    {/* {this.state.filteredeventbookings.map(row =>
                                        <TableRow>
                                            <TableCell>Event</TableCell>
                                            <TableCell>{row.type}</TableCell>
                                            <TableCell>{row.time}</TableCell>
                                            <TableCell>-</TableCell>
                                            <TableCell>Remark</TableCell>
                                        </TableRow>    
                                    )} */}
                                </TableBody>
                            </Table>
                        </TableContainer>
                    </Paper>
                </Box>
            </div>
        );
    }
}
 
export default MyBookings;

