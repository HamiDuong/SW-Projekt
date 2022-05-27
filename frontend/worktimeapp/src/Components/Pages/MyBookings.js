import React, {Component} from 'react';
import { 
    RadioGroup,
    Radio, 
    FormControlLabel, 
    FormControl, 
    FormLabel, 
    TableHead, 
    TableSortLabel, 
    TableRow, 
    TableCell, 
    TableContainer,
    Box,
    Paper,
    Table,
    TableBody,
    Button
} from '@mui/material';
import TextField from '@mui/material/TextField';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';

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
        start:'8:00',
        end:'',
        remarks:''
    },
    {
        bookingtype:'Event',
        type:'Work',
        start:'',
        end:'18:00',
        remarks:''
    },
    {
        bookingtype:'Time Interval',
        type:'Work',
        start:'8:00',
        end:'18:00',
        remarks:''
    },
    {
        bookingtype:'Event',
        type:'Break',
        start:'12:00',
        end:'',
        remarks:''
    },
    {
        bookingtype:'Time Interval',
        type:'Break',
        start:'12:00',
        end:'',
        remarks:'Open Interval, no End Event'
    },
    {
        bookingtype:'',
        type:'',
        start:'',
        end:'',
        remarks:''
    },
    {
        bookingtype:'',
        type:'',
        start:'',
        end:'',
        remarks:''
    },
                    
]

class MyBookings extends Component {
    constructor(props){
        super(props);
        this.state = {
            bookings: [],
            typefilter: '',
            bookingtype: null,
            startfilter: null,
            endfilter: null, 
            loadingInProgress: false,
            error: null,
        }
    }

    handleChange = (e) => {
        this.setState({ [e.target.name] : e.target.value });}

    render(){
        const {} = this.state;
        return(
            <div>
                <h1>My Bookings</h1>
                <TextField
                    id="standard-basic"
                    label="Start Date"
                    variant="standard"
                    padding='10px'
                />
                <TextField id="standard-basic" label="End Date" variant="standard" />
                <FormControl sx={{ minWidth: 258}}>
                    <InputLabel>Type</InputLabel>
                    <Select
                    name='intervaltype'
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
                <Button>
                    Filter
                </Button>

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
                                        <TableRow>
                                            <TableCell>{row.bookingtype}</TableCell>
                                            <TableCell>{row.type}</TableCell>
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