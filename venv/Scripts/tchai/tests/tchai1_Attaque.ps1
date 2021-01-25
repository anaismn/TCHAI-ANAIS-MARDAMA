#!/bin/sh

$oldMontant=$args[0]
$newMontant=$args[1]
$file=$args[2]
(Get-Content $file) |
Foreach-Object {$_.replace($oldMontant, $newMontant)} |
Set-Content $file
