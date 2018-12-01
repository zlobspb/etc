#!/usr/bin/env perl

use strict;
use AnyEvent::Handle;
use AnyEvent::Socket;
use EV;
use MIME::Base64 'encode_base64';

sub b64($) {
    my $enc = encode_base64($_[0]);
    $enc =~ s{\r?\n}{}sg;
    return $enc;
}

my $user = 'mazafaka14@hotmail.com';
my $token = 'abracadabra';
my $server = 'imap-mail.outlook.com';

tcp_connect $server,993, sub {
    my $fh = shift or return;
    my $h = AnyEvent::Handle->new(
        fh => $fh,
    );
    $h->starttls('connect');
    my $sent = 0;
    $h->on_read(sub {
        warn $h->{rbuf};
        $h->{rbuf} = '';
        unless ($sent++) {
            my $X = "\x01";
            my $buf = "A01 AUTHENTICATE XOAUTH2 ".b64(
                "user=$user${X}auth=Bearer $token${X}${X}"
            )."\r\n";

            warn "BUF: $buf";

            $h->push_write($buf);
        }
    });
};

EV::loop;
