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
import CreateWorkTimeSheet from '../Dialog/CreateWorkTimeSheet';

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
            userId : this.props.userId,

            intervalbookings: [],
            eventbookings: [],

            filteredintervalbookings: [],
            filteredeventbookings: [],

            renderedbookings: [],

            workbookings: [],

            bookingtype: 'all',
            typefilter: null,
            startfilter: null,
            endfilter: null,

            loadingInProgress: false,
            showResetButton: true,
            error: null,

            dialogWorkTimeSheet: false,
            showEditWindow: false
        }
    }

    componentDidMount(){
        console.log('ComponentDidMount')
        this.getBookings();
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

    getBookings = () => {
        // WorkTimeAppAPI.getAPI().getAllBookingsForUser(this.props.userId).then(responseJSON =>
        // // hier muss Mihris Booking Methode rein um alle Buchungen eines Users zu holen
        //     this.setState({
        //         intervalbookings: responseJSON.timeintervals,
        //         eventbookings: responseJSON.events,
        //         filteredintervalbookings: responseJSON.timeintervals,
        //         filteredeventbookings: responseJSON.events            
        //     },function(){
        //         console.log("getBookings")
        //     }))

            // hier muss Mihris Booking Methode rein um alle Buchungen eines Users zu holen
                
            this.setState({
                    intervalbookings: fakebackend.timeintervals,
                    eventbookings: fakebackend.events,
                    filteredintervalbookings: fakebackend.timeintervals,
                    filteredeventbookings: fakebackend.events            
                },function(){
                    console.log("getBookings")
                })

                //von den Bookings nur die Work Intervalle rausfiltern
                let res = [];
                let bookings = this.state.intervalbookings;
                bookings.forEach(elem => {
                    if(elem.type == "Work"){
                        res.push(elem);
                    }
                });
                this.setState({
                    workbookings: res
                }, function(){
                    console.log("Workbookings wurden ausgefiltert")
                })
    }

    getWorkBookings = () => {
        let res = [];
        let bookings = this.state.intervalbookings;
        bookings.forEach(elem => {
            if(elem.type == "Work"){
                res.push(elem);
                console.log(elem.type)
            }
        });
        this.setState({
            workbookings: res
        }, function(){
            console.log("Workbookings wurden ausgefiltert")
        })
    }

    resetFilter = () => {
        this.setState({
            bookingtype: 'all',
            typefilter: '',
            startfilter: null,
            endfilter: null,
            showResetButton: true,
            filteredintervalbookings: this.state.intervalbookings,
            filteredeventbookings: this.state.eventbookings
        }, function(){
            console.log("State wurde zurückgesetzt")
        })
    }

    filterBookings = () => {

        let starthold = document.getElementById("startfilter");
        let endhold = document.getElementById("endfilter");
        let type = this.state.typefilter

        this.setState({
            startfilter: starthold.value,
            endfilter: endhold.value,
            showResetButton: false
        }, function(){
            console.log("Zeitfilter wurden gesetzt");
        });

        let intervalbookings = this.state.intervalbookings;
        let ires = [];
        let eventbookings = this.state.eventbookings;
        let eres = [];

        //Buchungen nach Type filtern
        //Intervallbuchungen nach Type filtern
        intervalbookings.forEach(function(elem){
            let elemtype = elem.type
            console.log(elemtype)
            if(type == elemtype){
                ires.push(elem)
                console.log('Elemt gehört in den Filter')
                console.log()
            }else{
                console.log('Element gehört nicht in das Filter')
            }

        })

        this.setState({
            filteredintervalbookings: ires
        }, function(){
            console.log("State wurde gesetzt für IntervalBuchungen nach TypeFilterung")
        })

        //Eventbuchungen nach Type filtern
        eventbookings.forEach(function(elem){
            let elemtype = elem.type
            console.log(elemtype)
            if(type == elemtype){
                eres.push(elem)
                console.log('Elemt gehört in den Filter')
            }else{
                console.log('Element gehört nicht in das Filter')
            }

        })

        this.setState({
            filteredeventbookings: eres
        }, function(){
            console.log("State wurde gesetzt für EventBuchungen nach TypeFilterung")
        })


        console.log(this.state.filteredintervalbookings)

        if(this.state.bookingtype == "timeinterval"){
            this.setState({
                filteredeventbookings: null
            },function(){
                console.log("Nur Timeintervalbuchungen")
            })
        }else if(this.state.bookingtype == "event"){
            this.setState({
                filteredintervalbookings: null
            }, function(){
                console.log("Nur Eventbuchungen")
            })
        }
    }
    
    editRow = (event) => {
        event.stopPropagation();
        this.setState({
            showEditWindow: true
        },function(){
            console.log("Editwindow wird geöffnet")
        })
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
            console.log("Open Create WorkTimeSheet Window")
        })
    }

    //TODO
    closeDialog = () => {
        if(true){
            this.setState({
                dialogWorkTimeSheet: false
            }, function(){
                console.log("Editwindow wird geschlossen")
            })
        }else{
            this.setState({
                showDialog: false
            },function(){
                console.log("Editwindow wird geschlossen ohne Update")
            })

        }
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
                <CreateWorkTimeSheet show = {this.state.dialogWorkTimeSheet} workbookings = {this.state.filteredintervalbookings} onClose={this.closeDialog}></CreateWorkTimeSheet>
            </>
        );
    }
}
 
export default MyBookings;

