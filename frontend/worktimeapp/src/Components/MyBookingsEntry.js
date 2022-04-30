import { TableContainer } from '@mui/material';
import React, {Component} from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';

class MyBookingsEntry extends Component {
    constructor(props) {
        super(props);
        this.state = {
            loadingInProgress: false,
            error: null,
        }
    }

    //Erstellung eines Eintrags in der Tabelle
    createEntry(type, name, start, ende){
        return {type, name, start, ende};
    }

    render() { 
        return (
            <div>
                <p>Hier startet ein Eintrag</p>
                    <Table aria-label="simple table">
                        <TableHead>
                        <TableRow>
                            <TableCell align="right">Name</TableCell>
                            <TableCell align="right">Start</TableCell>
                            <TableCell align="right">Ende</TableCell>
                        </TableRow>
                        </TableHead>
                    </Table>
            </div>


        );
    }
}
 
export default MyBookingsEntry;