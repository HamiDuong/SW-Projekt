import React, {Component} from 'react';
import { 
    FormControl, 
    TableHead, 
    TableRow, 
    TableCell, 
    TableContainer,
    Box,
    Paper,
    Table,
    TableBody,
    Button,
    FormControlLabel,
    Radio,
    FormLabel,
    RadioGroup,
    TextField,
    InputLabel,
    MenuItem,
    Select
} from '@mui/material';

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
/*     {
        id: 'date',
        name: 'Date',
        numeric: false,
        disablePadding: false,
        label: 'Date'
    }, */
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
    },
    {
        id: 'remarks',
        name: 'Remarks',
        numeric: false,
        disablePadding: false,
        label: 'Remarks'
    }
]

const bookings = [
    {
        bookingtype:'Event',
        type:'Work',
        date: new Date('1995-12-17T03:24:00').toLocaleString(),
        start: new Date('2022-05-05T08:30:00').toLocaleString(),
        end:'-',
        remarks:''
    },
    {
        bookingtype:'Event',
        type:'Work',
        date: new Date('1995-12-17T03:24:00').toLocaleString(),
        start:'-',
        end: new Date('2022-05-05T18:30:00').toLocaleString(),
        remarks:''
    },
    {
        bookingtype:'Time Interval',
        type:'Work',
        date: new Date('1995-12-17T03:24:00').toLocaleString(),
        start:new Date('2022-05-05T08:30:00').toLocaleString(),
        end:new Date('2022-05-05T18:30:00').toLocaleString(),
        remarks:''
    },
    {
        bookingtype:'Event',
        type:'Break',
        date: '2022-05-05',
        start:'12:00',
        end:'-',
        remarks:''
    },
    {
        bookingtype:'Time Interval',
        type:'Break',
        date: '2022-05-05',
        start:'12:00',
        end:'EMPTY',
        remarks:'Open Interval, no End Event'
    },                    
]

let intervalbookings = [
    {
        id: '1',
        dateoflastchange: new Date('2022-05-05T18:30:00').toLocaleString(),
        start: new Date('2022-05-05T08:30:00').toLocaleString(),
        end: new Date('2022-05-05T18:30:00').toLocaleString(),
        startevent: '1',
        endevent: '2',
        type: 'Work'
    },
    {
        id: '2',
        dateoflastchange: new Date('2022-05-05T12:30:00').toLocaleString(),
        start: new Date('2022-05-05T12:30:00').toLocaleString(),
        end: null,
        startevent: '1',
        endevent: null,
        type: 'Break'
    }
]

// let eventbookings = [
//     {
//         id: '1',
//         dateoflastchange: new Date('2022-05-05T08:30:00'),
//         time: new Date('2022-05-05T08:30:00')
//     },
//     {
//         id: '2',
//         dateoflastchange: new Date('2022-05-05T18:30:00'),
//         time: new Date('2022-05-05T18:30:00')
//     },
//     {
//         id: '1',
//         dateoflastchange: new Date('2022-05-05T12:30:00'),
//         time: new Date('2022-05-05T12:30:00')
//     }
// ]


// let work = WorkBO(new Date('1995-12-17T03:24:00').toLocaleString(), new Date('1995-12-17T03:24:00').toLocaleString(), 1, 2, 'Work');
// let pause = BreakBO(new Date('1995-12-17T03:24:00').toLocaleString(), new Date('1995-12-17T03:24:00').toLocaleString(), 1, 2, 'Work')

// let hold = [
//     work,
//     pause
// ]

/***
 * Steps:
 * alle Eventbuchungen des Users holen -> eventbookingsmit mit EventSubklassenBO
 * alle Intervalbuchungen des Users holen -> intervalbookings mit IntervalSubklassenBO
 * 
 * umwandeln in Date: new Date(this.state.startfilter)
 */

class MyBookings extends Component {
    constructor(props){
        super(props);
        this.state = {
            intervalbookings: [],
            eventbookings: [],

            filterdintervalbookings: [],
            filterdeventbookings: [],

            bookingtype: 'all',
            typefilter: '',
            startfilter: null,
            endfilter: null,

            loadingInProgress: false,
            showResetButton: true,
            error: null,
        }
    }

    handleChange = ev => {
        this.setState({ [ev.target.name] : ev.target.value });
    };

    print = () => {
        console.log(this.state.bookingtype);
        console.log(this.state.typefilter);
        this.setState({
            showResetButton: false
        })
        console.log(this.state.showResetButton);
        console.log(this.state.startfilter);
        console.log(this.state.endfilter);
    }

    componentDidMount(){
        //Methoden welche direkt aufgerufen werden sollen beim Instanziieren des Objects
    }

    setFilter = () => {
        let starthold = document.getElementById("startfilter");
        let endhold = document.getElementById("endfilter");
        this.setState({
            startfilter: starthold.value,
            endfilter: endhold.value,
            showResetButton: false
        }, function(){
            console.log(this.state.startfilter);
        });
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
        console.log(this.state.bookingtype);
        console.log(this.state.typefilter);
        console.log(this.state.startfilter);
        console.log(this.state.endfilter);
    }

    getIntervalBookings = () => {

    }

    makeRows = () => {
        let holder = this.state.bookings;
        let res = []
        holder.forEach(elem => {
            let p = {
                bookingtype: "Interval",
                type: elem.type,
                start: elem.start.toLocaleString(),
                end: elem.end.toLocaleString(),
                remarks: ""
            }
            res.append(p);
        })
        this.state({
            intervalbookings: res
        })
        
    }

    getEventBookings = () => {

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
                        onClick={this.setFilter}
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
                                        bookings.map( row =>
                                        <TableRow
                                            hover true
                                        >
                                            {/* <TableCell>{row.type}</TableCell>
                                            <TableCell>{row.start}</TableCell>
                                            <TableCell>{row.end}</TableCell> */}

                                            <TableCell>{row.bookingtype}</TableCell>
                                            <TableCell>{row.type}</TableCell>
                                            <TableCell>{row.date}</TableCell>
                                            <TableCell>{row.start}</TableCell>
                                            <TableCell>{row.end}</TableCell>
                                            <TableCell>{row.remarks}</TableCell>

                                        </TableRow>
                                        )
                                    }
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