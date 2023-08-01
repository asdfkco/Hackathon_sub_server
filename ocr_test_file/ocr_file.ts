// @ts-ignore
import { Column, Entity, PrimaryColumn } from "typeorm";

@Entity()
export default class PhysicalData {
  @PrimaryColumn({ type: "varchar", comment: "google_oauth id" })
  id: number;

  @Column({ type: "int", comment: "신장" })
  height: number;

  @Column({ type: "int", comment: "나이" })
  ages: number;

  @Column({ type: "datetime", comment: "기입일자" })
  inspection_date: Date;

  // 체성분 분석 5요소.
  @Column({ type: "int", comment: "체수분" })
  body_water: number;

  @Column({ type: "int", comment: "단백질" })
  protein: number;

  @Column({ type: "int", comment: "무기질" })
  minerals: number;

  @Column({ type: "int", comment: "체지방" })
  body_fat: number;

  @Column({ type: "int", comment: "체중" })
  weight: number;

  // 골격근량
  @Column({ type: "int", comment: "골격근량" })
  skeletal_muscle_mass: number;

  // 비만분석 2요소.
  @Column({ type: "int", comment: "bmi 지수" })
  bmi: number;

  @Column({ type: "int", comment: "체지방률" })
  body_fat_percentage: number;

  @Column({ type: "int", comment: "성장/인바디 점수" })
  inbody_score: number;
}