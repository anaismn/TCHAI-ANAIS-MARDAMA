#!/bin/sh

$index=$args[0]
$file=$args[1]
$lines = Get-Content $file
$lineDel = $lines[$index]
$lines | where { $_ -ne $lineDel } | Set-Content $file