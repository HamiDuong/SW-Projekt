import { TableContainer } from '@mui/material';
import React, {Component} from 'react';
import Table from '@mui/material/Table';
// import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';

class MyBookingsEventEntry extends Component {
    constructor(props) {
        super(props);
        this.state = {
            booking: props.booking,

            loadingInProgress: false,
            error: null,
        }
    }

    //Erstellung eines Eintrags in der Tabelle

    render() { 
        return (
            <TableRow
                hover
                onClick = {() => console.log("Click")}
            >
                <TableCell>Interval</TableCell>
                <TableCell>{this.state.booking.type}</TableCell>
                <TableCell>{this.state.booking.time}</TableCell>
                <TableCell>-</TableCell>
                <TableCell>Remark</TableCell>

            </TableRow>
        );
    }
}
 
export default MyBookingsEventEntry;