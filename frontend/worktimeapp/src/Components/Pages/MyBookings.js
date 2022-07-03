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

            workbookings: [],

            bookingtype: 'timeinterval',
            typefilter: null,
            startfilter: null,
            endfilter: null,

            loadingInProgress: false,
            showResetButton: true,
            showFilterButton: false,
            error: null,

            holdintervalbooking: null,
            holdeventbooking: null,
            holdeventbooking2: null,

            dialogWorkTimeSheet: false,
            showEditWindow: true
        }
    }

    // After component mounted following function will be executed: the booked bookings of the user and the work bookings will be saved in state
    componentDidMount() {
        console.log('ComponentDidMount');
        this.getBookings();
    }


    // Save changes buttons and textfields into state
    handleChange = ev => {
        this.setState({ [ev.target.name]: ev.target.value });
    };



    // Gets all booked bookings of the current user
    getBookings = () => {
        WorkTimeAppAPI.getAPI().getAllTimeintervalsForUser(this.props.userId).then(responseJSON =>
            this.setState({
                intervalbookings: responseJSON,
                filteredintervalbookings: responseJSON,
            }, function () {
                let work = responseJSON;
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

        WorkTimeAppAPI.getAPI().getAllEventsForUser(this.props.userId).then(responseJSON =>
            this.setState({
                eventbookings: responseJSON,
                filteredeventbookings: responseJSON
            }, function () {
                console.log(this.state.eventbookings);
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
                    this.state.filteredintervalbookings.map(row => <MyBookingsIntervalEntry key={row.id + " " + row.type} onClose1={this.closeEditDialog} booking={row} userId={this.props.userId} />)
                }
            </TableBody>
        )
    }

    // Map table rows for event bookings
    mapEventBookings = () => {
        return (
            <TableBody>
                {
                    this.state.filteredeventbookings.map(row => <MyBookingsEventEntry key={row.id + " " + row.type + "1"} onClose1={this.closeEventEditDialog} booking={row} userId={this.props.userId} />)
                }
                {/* {
                    this.state.filteredeventbookings2.map(row => <MyBookingsEventEntry key = {row.id + " " + row.type+ "2"} onClose1={this.closeEventEditDialog} booking={row} userId={this.props.userId} />)
                } */}
            </TableBody>
        )
    }

    //Callback Funktion to confirm when forEach is finished
    callBack() {
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
        console.log("INterval", this.state.intervalbookings);
        console.log("event", this.state.eventbookings);
        console.log("event2", this.state.eventbookings2);

        WorkTimeAppAPI.getAPI().getAllTimeIntervalsWithinTimeFrame(this.state.userId, starthold.value, endhold.value).then(responseInterval =>
            this.setState({
                filteredintervalbookings: responseInterval
            }, function () {
                console.log("Got Intervalbookings")
            })
        )

        WorkTimeAppAPI.getAPI().getAllEventsWithinTimeFrame(this.state.userId, starthold.value, endhold.value).then(responseEvents =>
            this.setState({
                filteredeventbookings: responseEvents
            }, function () {
                console.log("Gor Eventbookings", responseEvents)
            })
        )

        let bookingstype = this.state.bookingtype
        console.log('Vergleich von Buchungsart');
        if (bookingstype == 'timeinterval') {
            this.setState({
                filteredeventbookings: []
            }, function () {
                console.log("Nur Timeintervalbuchungen mit verknüpften Events");
            })
        } else if (bookingstype == 'event') {
            this.setState({
                filteredintervalbookings: [],
            }, function () {
                console.log("Nur Eventbuchungen");
            })
        }

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
                            <FormControlLabel value="timeinterval" control={<Radio />} label="Time Intervals" />
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