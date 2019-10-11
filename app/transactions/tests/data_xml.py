xml_sample = """<?xml version="1.0" encoding="UTF-8"?>
<root>
   <_id>589c493e5f2687111bb6d800</_id>
   <additive_tax_money>
      <amount>0</amount>
      <currency>JOD</currency>
   </additive_tax_money>
   <business_id>3f522ee8-7e69-4d78-aeb5-5278aaf21558</business_id>
   <creation_time>2017-02-09T10:49:34.000Z</creation_time>
   <creator>
      <email>anonymous@example.com</email>
      <id>00000000-0000-0000-0000-000000000000</id>
      <name>John Doe</name>
   </creator>
   <dining_option>In-House</dining_option>
   <discount_money>
      <amount>0</amount>
      <currency>JOD</currency>
   </discount_money>
   <inclusive_tax_money>
      <amount>483</amount>
      <currency>JOD</currency>
   </inclusive_tax_money>
   <itemization>
      <list-item>
         <category>
            <id>a9895c94-15cc-4db1-bbad-fe62d218c931</id>
            <name>Appetizers</name>
         </category>
         <discount_money>
            <amount>0</amount>
            <currency>JOD</currency>
         </discount_money>
         <discounts />
         <gross_sales_money>
            <amount>3017</amount>
            <currency>JOD</currency>
         </gross_sales_money>
         <id>788cb9cb-106f-4d32-ac48-df9e8433ff50</id>
         <modifiers>
            <list-item>
               <applied_money>
                  <amount>0</amount>
                  <currency>JOD</currency>
               </applied_money>
               <id>7424ae3d-36bc-4c0c-b790-310614905aed</id>
               <name>6 Pieces</name>
               <quantity>1</quantity>
            </list-item>
         </modifiers>
         <name>Boneless Chicken Wings</name>
         <net_sales_money>
            <amount>3017</amount>
            <currency>JOD</currency>
         </net_sales_money>
         <quantity>1</quantity>
         <single_quantity_money>
            <amount>3500</amount>
            <currency>JOD</currency>
         </single_quantity_money>
         <taxes>
            <list-item>
               <applied_money>
                  <amount>483</amount>
                  <currency>JOD</currency>
               </applied_money>
               <id>cfc92a12-f847-4942-b6ec-1454d194c9ba</id>
               <inclusion_type>INCLUSIVE</inclusion_type>
               <is_custom_amount>true</is_custom_amount>
               <name>Sales Tax</name>
               <rate>0.16</rate>
            </list-item>
         </taxes>
         <total_money>
            <amount>3500</amount>
            <currency>JOD</currency>
         </total_money>
         <variation>
            <id>37b64192-6b0f-479d-aeee-3c382a0671b9</id>
            <name>Plate</name>
            <price_money>
               <amount>3500</amount>
               <currency>JOD</currency>
            </price_money>
            <pricing_type>FIXED</pricing_type>
         </variation>
      </list-item>
   </itemization>
   <location_id>96e9975b-b1bf-47ee-aeaf-63518022e95e</location_id>
   <receipt_id>Cj9uohMQNVflSq7taYtVRk</receipt_id>
   <refunded_money>
      <amount>0</amount>
      <currency>JOD</currency>
   </refunded_money>
   <serial_number>C1-498</serial_number>
   <tax_money>
      <amount>483</amount>
      <currency>JOD</currency>
   </tax_money>
   <taxes>
      <list-item>
         <applied_money>
            <amount>483</amount>
            <currency>JOD</currency>
         </applied_money>
         <id>cfc92a12-f847-4942-b6ec-1454d194c9ba</id>
         <inclusion_type>INCLUSIVE</inclusion_type>
         <is_custom_amount>true</is_custom_amount>
         <name>Sales Tax</name>
         <rate>0.16</rate>
      </list-item>
   </taxes>
   <tender>
      <name>CASH</name>
      <total_money>
         <amount>3500</amount>
         <currency>JOD</currency>
      </total_money>
      <type>CASH</type>
   </tender>
   <tip_money>
      <amount>0</amount>
      <currency>JOD</currency>
   </tip_money>
   <total_collected_money>
      <amount>3500</amount>
      <currency>JOD</currency>
   </total_collected_money>
   <transaction_id>37a5f57a-48bc-483d-91b7-88c8b1b9509c</transaction_id>
</root>"""
