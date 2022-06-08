import React, { Component } from 'react';
import { Button, Table, TableBody, TableCell, TableHead, TableRow } from '@mui/material';
import { Box } from '@mui/system';
import { TableContainer } from '@mui/material';
import Paper from '@mui/material/Paper';
import TablePagination from '@mui/material/TablePagination';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';

class OverTimeEntry extends Component {
    constructor(props) {
        super(props);
        this.state = {
            project: 'Neues Projekt',
            activities: [],
            capacity: [],
            current_capacity: '',
            bookedTime: { 'Use Case erstellen': [1, 'Max Mustermann'], 'Malen': [2, 'Max Musterfrau'], 'Basteln': [3, 'Maxeuso deMustermann'], 'Kaffee trinken': [4, 'Max Musterfrau'], 'React hassen': [5000, 'Max Musterfrau'] },
            employees: '',
            activity_names: ''

        }
    }

    componentDidMount() {
        this.getActivities()
        this.newfunc()
    }

    getActivities = () => {
        WorkTimeAppAPI.getAPI().getAllActivities().then(activity =>
            this.setState({
                activities: [...this.state.activities, activity],
            }, this.getCapacities(activity),
                this.getCurrentCapacities(activity),
                this.getActivityNames(activity)
            ))
    }


    getCapacities = (arr) => {
        const acti = this.state.activities
        let i = 0
        while (i <= acti.length) {
            console.log('Hier', arr[i].capacity)
            this.setState({
                capacity: [...this.state.capacity, arr[i].capacity]
            }, function () {
                console.log(this.state.capacity)
            })
            i = i + 1
        }
    }

    getCurrentCapacities = (arr) => {
        const acti = this.state.activities
        let i = 0
        while (i <= acti.length) {
            console.log('before sS CC', arr[i].current_capacity)
            this.setState({
                current_capacity: [...this.state.current_capacity, arr[i].current_capacity]
            }, function () {
                console.log('CC', this.state.current_capacity)
            })
            i = i + 1
        }
    }

    getActivityNames = (arr) => {
        const acti = this.state.activities
        let i = 0
        while (i <= acti.length) {
            console.log('AN before sS', arr[i].name)
            this.setState({
                activity_names: [...this.state.activity_names, arr[i].name]
            }, function () {
                console.log('AN', this.state.activity_names)
            })
            i = i + 1
        }
    }

    columns() {
        const columns = [
            {
                id: 'Activity',
                label: 'activties',
                minWidth: 170
            },
            {
                id: 'capacity',
                label: 'capacity (h)',
                minWidth: 100
            },
            {
                id: 'current_capacity',
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

        return columns
    }

    BoilingVerdict() {
        const rows = this.smth()
        const columns = this.columns()

        if (this.props.celsius == this.state.project) {
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
                                            Project: {this.props.temperature}
                                        </TableCell>
                                        <TableCell align="left" colSpan={6}>
                                            Details
                                        </TableCell>
                                    </TableRow>
                                    <TableRow>
                                        TableRow
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
                                    TableBody
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
    };


    newfunc() {
        const activities2 = this.state.activities
        const bookedTime = this.state.capacity
        const planedTime = this.state.planedTime
        const activities = []
        const planedTime2 = []
        const bookedTimes = []
        const employees = []

        for (var key in activities2) {
            //console.log('hier sind die Activities zu Project A: ', activities[key])
            activities.push(key)
        } //console.log('AKTIVITÄTEN ', activities)

        for (var key in planedTime) {
            //console.log('hier sind die geplanten Zeiten', planedTime[key][0])
            planedTime.push(planedTime2[key][0])

        } //console.log('ZEITEN ', planedTime)

        for (var key in planedTime) {
            //console.log('hier sind die geplanten Zeiten', planedTime[key][0])
            employees.push(planedTime[key][1])

        } //console.log('ZEITEN ', planedTime)

        for (var key in bookedTime) {
            //console.log(key, bookedTime[key])
            bookedTimes.push(bookedTime[key][0])
        }
    }

    createData(activity, capacity, current_capacity) {
        const delta = capacity - current_capacity;
        return { activity, capacity, current_capacity, delta };
    }

    smth() {
        let newthingy = []
        const activities = this.state.activity_names
        const planedTimes = this.state.capacity
        const bookedTimes = this.state.current_capacity
        const employees = []

        for (var i = 0; i <= activities.length; i++) {
            let new_data = this.createData(activities[i], planedTimes[i], bookedTimes[i])
            newthingy.push(new_data)
        }

        console.log('Newthing', newthingy[0])
        return newthingy
    }


    render() {
        const rows = this.smth()
        const columns = this.columns()
        return (
            <diV>
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
                                            Project: {this.state.temperature}
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
                                    {rows.map((row) => {
                                        return (
                                            <TableRow hover  >
                                                {columns.map((column) => {
                                                    const value = row[column];
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
            </diV>
        );
    }

}

export default OverTimeEntry;