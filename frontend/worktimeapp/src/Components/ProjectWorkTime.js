import React, { Component } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';

class ProjectWorktTime extends Component {
    constructor(props) {
        super(props);
    }
    state = {}
    render() {
        return (
            <Table >
                <TableHead>
                    <TableRow>
                        <TableCell align="right">Tag</TableCell>
                        <TableCell align="right">Sollstundensatz</TableCell>
                        <TableCell align="right">Iststundensatz</TableCell>
                    </TableRow>
                </TableHead>
            </Table>
        );
    }
}

export default ProjectWorktTime;
