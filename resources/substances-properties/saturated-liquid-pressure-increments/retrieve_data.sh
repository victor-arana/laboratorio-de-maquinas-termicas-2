#!/bin/bash

DIGITS=$1
P_LOW=$2
P_HIGH=$3
P_INCREMENT=$4
DESTINATION=$5
PRESSURE=$8
#IDs:
#    C811972: 134a    
ID=$6 
#Types:
#    SatT - Saturation temperature increments
#    SatP - Saturation pressure increments
#    IsoBar - Isobaric
TYPE=$7
if [ "$TYPE" = "SatT" ]; then
    URL="https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=$ID&Type=$TYPE&Digits=$DIGITS&PLow=$P_LOW&PHigh=$P_HIGH&PInc=$P_INCREMENT&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm"
echo $URL
else 
    if [ "$TYPE" = 'IsoBar' ]; then
	    URL="https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=$ID&Type=$TYPE&Digits=$DIGITS&P=$PRESSURE&THigh=$P_HIGH&TLow=$P_LOW&TInc=$P_INCREMENT&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm"
    fi
    echo $URL
fi
curl --silent --output $DESTINATION-tmp.csv $URL
# 1: Temperature [C]
# 2: Pressure [bar]
# 3: Density [kg/m^3]
# 4: Volume [m^3/kg]
# 5: Internal Energy [kJ/kg]
# 6: Enthalpy [kJ/kg]
# 7: Entropy [J/g*K]
awk '{print $2, $1, $4, $5, $6, $7}' "$DESTINATION-tmp.csv" | tail +2 > "$DESTINATION.csv"
rm "$DESTINATION-tmp.csv"  
