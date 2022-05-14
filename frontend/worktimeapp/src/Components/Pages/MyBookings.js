import React, {Component} from 'react';
import { RadioGroup, Radio, FormControlLabel, FormControl, FormLabel, TableHead, TableSortLabel, TableRow } from '@mui/material';
import TextField from '@mui/material/TextField';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';

const header = [
    {
        id: 'bookingtype',
        numeric: false,
        disablePadding: true,
        label: 'Event/ Interval'
    },
    {
        id: 'type',
        numeric: false,
        disablePadding: true,
        label: 'Type'
    },
    {
        id: 'start',
        numeric: true,
        disablePadding: true,
        label: 'Start Date'
    },
    {
        id: 'end',
        numeric: true,
        disablePadding: true,
        label: 'End Date'
    },
    {
        id: 'remarks',
        numeric: false,
        disablePadding: true,
        label: 'Remarks'
    }
]

class MyBookings extends Component {
    constructor(props){
        super(props);
        this.state = {
            bookings: [],
            loadingInProgress: false,
            error: null,
        }
    }

    handleChange = (e) => {
        this.setState({ [e.target.name] : e.target.value });
    }

    static get header(){
        return header;
    }

    createRow(){
        var erg = {};
        return erg;
    }

    render(){
        const {} = this.state;
        return(
            <div>
                <h1>My Bookings</h1>
                <TextField id="standard-basic" label="Start Date" variant="standard" />
                <TextField id="standard-basic" label="End Date" variant="standard" />
                <FormControl sx={{ minWidth: 258}}>
                    <InputLabel id="demo-simple-select-label">Type</InputLabel>
                    <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value=""
                    label="Age"
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

                <TableHead>
                    <TableRow>
                    </TableRow>
                </TableHead>

            </div>
        );
    }
}
 
export default MyBookings;