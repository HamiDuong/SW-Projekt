import React, { Component } from 'react';
import TableCell from '@mui/material/TableCell';
import TableRow from '@mui/material/TableRow';
import EditBookingEvent from './Dialog/EditBookingEvent';

/**
 * @author Ha Mi Duong (https://github.com/HamiDuong)
 * 
 * Erstellung eines Eintrags für Eventbuchungen
 */
class MyBookingsEventEntry extends Component {
    constructor(props) {
        super(props);
        this.state = {
            booking: props.booking,
            showDialog: false,
            loadingInProgress: false,
            error: null,
        }
    }

    // Dialog zur Bearbeitung öffnen
    showEdit = () => {
        this.setState({
            showDialog: true
        }, function () {
            console.log("EditWindow öffnen per OnClick")
        })
    }

    // Dialog zur Bearbeitugn schließen
    closeEditDialog = (booking) => {
        if (booking) {
            this.setState({
                booking: booking,
                showDialog: false
            }, function () {
                console.log("Editwindow wird geschlossen")
                this.props.onClose1(booking)
            })
        } else {
            this.setState({
                showDialog: false
            }, function () {
                console.log("Editwindow wird geschlossen ohne Update")
            })

        }
    }

    // Debugging sobald die Komponente geladen ist
    componentDidMount() {
        console.log(this.state.booking)
    }

    // Änderungen in den gerenderten Komponenten werden im State abgespeichert
    handleChange = ev => {
        this.setState({ [ev.target.name]: ev.target.value });
    };

    render() {
        const { booking } = this.state
        return (
            <>
                <TableRow
                    hover
                    onClick={this.showEdit}
                >
                    <TableCell>Event</TableCell>
                    <TableCell>{this.state.booking.type}</TableCell>
                    <TableCell>{this.state.booking.time}</TableCell>
                    <TableCell>-</TableCell>
                </TableRow>
                <EditBookingEvent show={this.state.showDialog} onClose={this.closeEditDialog} booking={booking} />
            </>
        );
    }
}

export default MyBookingsEventEntry;