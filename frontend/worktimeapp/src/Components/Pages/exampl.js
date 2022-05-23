import React, { Component } from 'react';
import { Button, Table, TableBody, TableCell, TableHead, TableRow } from '@mui/material';
import { Box } from '@mui/system';
import { TableContainer } from '@mui/material';
import Paper from '@mui/material/Paper';
import TablePagination from '@mui/material/TablePagination';

const project = 'project A'
const activities2 = { 'Use Case erstellen': [1, 'Max Mustermann'], 'Malen': [2, 'Max Musterfrau'], 'Basteln': [3, 'Maxeuso deMustermann'], 'Kaffee trinken': [4, 'Max Musterfrau'], 'React hassen': [5000, 'Max Musterfrau'] }
const plannedTime = { 'Use Case erstellen': [1, 'Max Mustermann'], 'Malen': [2, 'Max Musterfrau'], 'Basteln': [3, 'Maxeuso deMustermann'], 'Kaffee trinken': [4, 'Max Musterfrau'], 'React hassen': [5000, 'Max Musterfrau'] }
const bookedTime = { 'Use Case erstellen': [1, 'Max Mustermann'], 'Malen': [2, 'Max Musterfrau'], 'Basteln': [2, 'Maxeuso deMustermann'], 'Kaffee trinken': [8, 'Max Musterfrau'], 'React hassen': [10000, 'Max Musterfrau'] }
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

const activities = []
const plannedTimes = []
const bookedTimes = []
const employees = []

for (var key in activities2) {
    //console.log('hier sind die Activities zu Project A: ', activities[key])
    activities.push(key)
} //console.log('AKTIVITÄTEN ', activities)

for (var key in plannedTime) {
    //console.log('hier sind die geplanten Zeiten', planedTime[key][0])
    plannedTimes.push(plannedTime[key][0])

} //console.log('ZEITEN ', planedTime)

for (var key in plannedTime) {
    //console.log('hier sind die geplanten Zeiten', planedTime[key][0])
    employees.push(plannedTime[key][1])

} //console.log('ZEITEN ', planedTime)

for (var key in bookedTime) {
    //console.log(key, bookedTime[key])
    bookedTimes.push(bookedTime[key][0])
}


function smth() {
    let newthingy = []
    for (var i = 0; i <= activities.length; i++) {
        let new_data = createData(activities[i], employees[i], plannedTimes[i], bookedTimes[i])
        newthingy.push(new_data)
    }
    return newthingy
}


const rows = smth()

function BoilingVerdict(props) {
    if (props.celsius == project) {
        return <div>
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
                                        Project: {project}
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
        </div >;
    }
    return <p>No Project selected.</p>;
}

export default BoilingVerdict;