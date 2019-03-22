@toc
# mysql
## 增
## 删
### 逻辑删除
一般的，删除要改为逻辑删除，使用update**，比如将status字段置为0
## 改
## 查
### 是否排序
 比如查询一个班级所有学生的信息，按名字排序，否则显得杂乱无章。
### 有效性
由于逻辑删除的关系，查询要检测对应的status字段是否有效。


# 设计接口的过程
 
相关sql分析过程
sql数据
sql测试语句


*****
<!--自定义  查询客房列表接口 --> <select id="selectGuestRoomList" parameterType="map" resultType="map">   select 
   de.equipment_no equipmentNo,
   g.guest_room_name guestRoomName,
   g.guest_room_id guestRoomId,
   g.is_lock bindStatus,
   r.name productName,
   dr.bind_time bindTime
  from guest_room_info g 
  left join room_product_info r on g.product_id = r.product_id
  left join door_lock_relation dr on g.guest_room_id = dr.guest_room_id
  left join door_lock_equipment_info de on de.equipment_id = dr.equipment_id
  where (de.status = 1 or de.status is null)
  and (g.status = 1 or g.status is null)
  <if test="guestRoomName != null and guestRoomName != ''">   and g.guest_room_name like concat('%',#{guestRoomName,jdbcType=VARCHAR},'%')
  </if>   <if test="productId != null and productId != ''">   and g.product_id=#{productId,jdbcType=VARCHAR}
  </if>   <if test="bindStatus == '1'.toString()">   and g.is_lock = '1'
   </if>   <if test="bindStatus == '0'.toString()">   and g.is_lock = '0'
   </if>   <if test="corpId != null and corpId != ''">   and r.corp_id=#{corpId,jdbcType=VARCHAR}
  </if>  </select>







***left join on**