DIGITS=$1
PRESSURE_LOW=$2
PRESSURE_HIGH=$3
PRESSURE_INCREMENT=$4
DESTINATION=$5
URL="https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C811972&Type=SatT&Digits=$DIGITS&PLow=$PRESSURE_LOW&PHigh=$PRESSURE_HIGH&PInc=$PRESSURE_INCREMENT&RefState=DEF&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=uPa*s&STUnit=N%2Fm"
echo $URL
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
