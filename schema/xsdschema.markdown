# XSD

*(Dieser Entwurf wird kontinuierlich verändert. Eine finale Version wird erst mit Version 1.0 veröffentlicht.)*

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" attributeFormDefault="unqualified"
           elementFormDefault="qualified">
    <xs:element name="libRML" type="libRMLType"/>

    <!-- libRMLType - Container for all -->
    <xs:complexType name="libRMLType">
        <!-- Contains only 1 subelement and a string 'version' -->
        <xs:sequence>
            <xs:element type="ItemType" name="item" minOccurs="1" maxOccurs="1"/>
        </xs:sequence>
        <xs:attribute type="xs:string" name="version"/>
    </xs:complexType>

    <!-- itemType - has many actions and some attributes -->
    <xs:complexType name="ItemType">
        <xs:sequence minOccurs="1" maxOccurs="unbounded">
            <xs:element type="ActionType" name="action"/>
        </xs:sequence>
        <xs:attribute type="xs:string" name="id"/>
        <xs:attribute type="xs:string" name="tenant"/>
        <xs:attribute type="xs:string" name="usageguide"/>
        <xs:attribute type="xs:string" name="template"/>
        <xs:attribute type="xs:boolean" name="mention"/>
        <xs:attribute type="xs:boolean" name="sharealike"/>
    </xs:complexType>

    <!-- ActionType - has many restrictions and some attributes -->
    <xs:complexType name="ActionType">
        <xs:sequence minOccurs="0" maxOccurs="unbounded">
            <xs:element type="RestrictionType" name="restriction"/>
        </xs:sequence>
        <xs:attribute name="type">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="displaymetadata"/>
                    <xs:enumeration value="read"/>
                    <xs:enumeration value="run"/>
                    <xs:enumeration value="lend"/>
                    <xs:enumeration value="download"/>
                    <xs:enumeration value="print"/>
                    <xs:enumeration value="reproduce"/>
                    <xs:enumeration value="modify"/>
                    <xs:enumeration value="reuse"/>
                    <xs:enumeration value="distribute"/>
                    <xs:enumeration value="publish"/>
                    <xs:enumeration value="archive"/>
                    <xs:enumeration value="index"/>
                    <xs:enumeration value="move"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute type="xs:boolean" name="permission"/>
    </xs:complexType>

    <!-- RestrictionType - all-in-one-mess -->
    <xs:complexType name="RestrictionType" mixed="true">
        <xs:sequence>
            <xs:element name="group" maxOccurs="unbounded" minOccurs="0" type="xs:string"/>
            <xs:element name="subnet" maxOccurs="unbounded" minOccurs="0">
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <!-- Regex for IPV4 incl. CDIR -->
                        <xs:pattern
                                value="^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(/(\d|[1-2]\d|3[0-2]))?$"/>
                        <!-- Regex for IPv6 -->
                        <xs:pattern
                                value="(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="machine" maxOccurs="unbounded" minOccurs="0">
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <!-- Regex for MAC-48 values -->
                        <xs:pattern value="^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="part" maxOccurs="unbounded" minOccurs="0" type="xs:string"/>
        </xs:sequence>
        <xs:attribute name="type">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="parts"/>
                    <xs:enumeration value="group"/>
                    <xs:enumeration value="age"/>
                    <xs:enumeration value="location"/>
                    <xs:enumeration value="date"/>
                    <xs:enumeration value="duration"/>
                    <xs:enumeration value="count"/>
                    <xs:enumeration value="concurrent"/>
                    <xs:enumeration value="watermark"/>
                    <xs:enumeration value="commercialuse"/>
                    <xs:enumeration value="quality"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute type="xs:date" name="fromdate"/>
        <xs:attribute type="xs:date" name="todate"/>
        <xs:attribute type="xs:nonNegativeInteger" name="maxresolution"/>
        <xs:attribute type="xs:string" name="maxbitrate"/>
        <xs:attribute type="xs:nonNegativeInteger" name="count"/>
        <xs:attribute type="xs:nonNegativeInteger" name="sessions"/>
        <xs:attribute type="xs:string" name="inside"/>
        <xs:attribute type="xs:string" name="outside"/>
        <xs:attribute type="xs:boolean" name="noncommercialuse"/>
        <xs:attribute type="xs:boolean" name="commercialuse"/>
        <xs:attribute type="xs:string" name="watermarkvalue"/>
        <xs:attribute type="xs:nonNegativeInteger" name="duration"/>
        <xs:attribute type="xs:nonNegativeInteger" name="minage"/>
    </xs:complexType>
</xs:schema>
```
