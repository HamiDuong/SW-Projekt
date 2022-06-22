import {
    TableContainer,
    Table,
    TableHead,
    TableRow,
    TableCell
 } from '@mui/material';
import React from 'react';


class WorkTimeUser extends Component {
    constructor(props) {
        super(props);
    }
    state = {  }
    render() { 
        return (
            <>
                <TableContainer>
                    <Table>
                        <TableHead>
                            <TableRow>
                                <TableCell
                                    key = 'date'
                                >Date</TableCell>
                                <TableCell
                                    key = 'coming'
                                >Coming</TableCell>
                                <TableCell
                                    key = 'going'
                                >Going</TableCell>
                                <TableCell
                                    key = 'workedTime'
                                >Worked Time</TableCell>
                                <TableCell
                                    key = 'contractTime'
                                >Contract Time</TableCell>

                            </TableRow>
                        </TableHead>
                    </Table>
                </TableContainer>
            </>
        );
    }
}
 
export default WorkTimeUser;