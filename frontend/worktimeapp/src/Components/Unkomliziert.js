import React, { Component } from 'react';
import { Button, Table, TableBody, TableCell, TableHead, TableRow } from '@mui/material';
import { Box } from '@mui/system';
import { TableContainer } from '@mui/material';
import Paper from '@mui/material/Paper';
import TablePagination from '@mui/material/TablePagination';



class Uncom extends Component {
    constructor(props) {
        super(props);
        this.state = {
            project: 'project A',
            activities2: { 'Use Case erstellen': [1, 'Max Mustermann'], 'Malen': [2, 'Max Musterfrau'], 'Basteln': [3, 'Maxeuso deMustermann'], 'Kaffee trinken': [4, 'Max Musterfrau'], 'React hassen': [5000, 'Max Musterfrau'] },
            plannedTime: { 'Use Case erstellen': [1, 'Max Mustermann'], 'Malen': [2, 'Max Musterfrau'], 'Basteln': [3, 'Maxeuso deMustermann'], 'Kaffee trinken': [4, 'Max Musterfrau'], 'React hassen': [5000, 'Max Musterfrau'] },
            bookedTime: { 'Use Case erstellen': [1, 'Max Mustermann'], 'Malen': [2, 'Max Musterfrau'], 'Basteln': [2, 'Maxeuso deMustermann'], 'Kaffee trinken': [8, 'Max Musterfrau'], 'React hassen': [10000, 'Max Musterfrau'] },
        }
    }

    state = {}
    render() {

        const activities = []
        const plannedTimes = []
        const bookedTimes = []
        const employees = []

        const columns = [
            {
                id: 'name',
                label: 'Activties',
                minWidth: 170
            },
            {
                id: 'plannedTime',
                label: 'planned Time (h)',
                minWidth: 100
            },
            {
                id: 'bookedTime',
                label: 'Booked Time (h)',
                minWidth: 170,
                align: 'right',
                format: (value) => value.toLocaleString('de-DE'),
            },
            {
                id: 'employee',
                label: 'Employee',
                minWidth: 170,
                align: 'right',
                format: (value) => value.toLocaleString('en-US'),
            },
            {
                id: 'delta',
                label: 'Delta (h)',
                minWidth: 170,
                align: 'right',
                format: (value) => value.toFixed(2),
            },
        ];

        function createData(name, employee, plannedTime, bookedTime) {
            const delta = plannedTime - bookedTime;
            return { name, employee, plannedTime, bookedTime, delta };
        }



        for (var key in this.state.activities2) {
            //console.log('hier sind die Activities zu Project A: ', this.state.activities[key])
            activities.push(key)
        } //console.log('AKTIVITÄTEN ', activities)

        for (var key in this.state.plannedTime) {
            //console.log('hier sind die geplanten Zeiten', this.state.planedTime[key][0])
            plannedTimes.push(this.state.plannedTime[key][0])

        } //console.log('ZEITEN ', planedTime)

        for (var key in this.state.plannedTime) {
            //console.log('hier sind die geplanten Zeiten', this.state.planedTime[key][0])
            employees.push(this.state.plannedTime[key][1])

        } //console.log('ZEITEN ', planedTime)

        for (var key in this.state.bookedTime) {
            //console.log(key, this.state.bookedTime[key])
            bookedTimes.push(this.state.bookedTime[key][0])
        }

        function smth() {
            let newthingy = []
            for (var i = 0; i <= activities.length; i++) {
                let new_data = createData(activities[i], employees[i], plannedTimes[i], bookedTimes[i])
                newthingy.push(new_data)
            }
            return newthingy
        }

        function projectn(props) {
            if (props.celsius == 'project A') {
                return <p>The water would boil.</p>;
            }
            return <p>The water would not boil.</p>;
        }


        const rows = smth()

        return (
            <div>
                <Box sx={{ margin: 3 }} style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                }}>
                    <Paper sx={{ width: '80%' }}>
                        <TableContainer sx={{ maxHeight: 440 }}>
                            <Table stickyHeader aria-label="sticky table">
                                <TableHead>
                                    <TableRow>
                                        <TableCell align="left" colSpan={0}>
                                            Project: {this.state.project}
                                        </TableCell>
                                        <TableCell align="left" colSpan={6}>
                                            Details
                                        </TableCell>
                                    </TableRow>
                                    <TableRow>
                                        {columns.map((column) => (
                                            <TableCell
                                                key={column.id}
                                                align={column.align}
                                                style={{ minWidth: column.minWidth }}
                                            >
                                                {column.label}
                                            </TableCell>
                                        ))}
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    {rows
                                        .map((row) => {
                                            return (
                                                <TableRow hover  >
                                                    {columns.map((column) => {
                                                        const value = row[column.id];
                                                        return (
                                                            <TableCell align={column.align}>
                                                                {column.format && typeof value === 'string'
                                                                    ? column.format(value)
                                                                    : value}
                                                            </TableCell>
                                                        );
                                                    })}
                                                </TableRow>
                                            );
                                        })}
                                </TableBody>
                            </Table>
                        </TableContainer>
                    </Paper>
                </Box>
            </div >
        );
    }
}

export default Uncom;
